import json
import os.path

import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials

from pymbbooth import config

def _auth(credential_file, scopes):
    """open browser to create credentials"""
    flow = InstalledAppFlow.from_client_secrets_file(
        credential_file, scopes=scopes
    )
 
    return flow.run_local_server(
        host="localhost",
        port=8181,
        authorization_prompt_message="",
        success_message="The auth flow is complete; you may close this window.",
        open_browser=True,
    )


def _save_cred(credentials, saved_credentials):
    cred_dict = {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "id_token": credentials.id_token,
        "scopes": credentials.scopes,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
    }

    with open(saved_credentials, "w") as fp:
        json.dump(cred_dict, fp)


def _get_authorized_session(credential_file, saved_credentials, scopes):
    if (
        not os.path.exists(saved_credentials)
        or os.path.getsize(saved_credentials) == 0
    ):
        creds = _auth(credential_file, scopes)
        session = AuthorizedSession(creds)
        _save_cred(creds, saved_credentials)
    else:
        creds = Credentials.from_authorized_user_file(
            saved_credentials, scopes
        )
        session = AuthorizedSession(creds)
    return session


def _get_albums(session):
    params = {"excludeNonAppCreatedData": True}
    while True:
        albums = session.get(
            "https://photoslibrary.googleapis.com/v1/albums", params=params
        ).json()
        if "albums" in albums:
            for a in albums["albums"]:
                yield a
            if "nextPageToken" in albums:
                params["pageToken"] = albums["nextPageToken"]
            else:
                return
        else:
            return

def get_album_id(session, album_name):
    for a in _get_albums(session):
        if a["title"].lower() == album_name.lower():
            return a["id"]
    # No matches, create new album
    create_album_body = json.dumps({"album": {"title": album_name}})
    resp = session.post(
        "https://photoslibrary.googleapis.com/v1/albums", create_album_body
    ).json()
    if "id" in resp:
        return resp["id"]
    else:
        return None


def setup_google_session():
    credential_file = "credentials.json"
    saved_credentials = "google_credentials.dat"
    scopes = [
        "https://www.googleapis.com/auth/photoslibrary",
        "https://www.googleapis.com/auth/photoslibrary.sharing",
    ]
    session = _get_authorized_session(credential_file, saved_credentials, scopes)
    return session
    

def upload_photo(session, photo_filename, album_id):
    session.headers["Content-type"] = "application/octet-stream"
    session.headers["X-Goog-Upload-Protocol"] = "raw"

    photo_path = os.path.join(config.PHOTO_DIR, photo_filename) 
    try:
        photo_file = open(photo_path, mode="rb")
        photo_bytes = photo_file.read()
    except OSError as err:
        print("Unable to read photo")

    session.headers["X-Goog-Upload-File-Name"] = photo_filename

    upload_token = session.post(
        "https://photoslibrary.googleapis.com/v1/uploads", photo_bytes
    )
    if (upload_token.status_code == 200) and upload_token.content:
        create_body = json.dumps(
            {
                "albumId": album_id,
                "newMediaItems": [
                    {
                        "description": "",
                        "simpleMediaItem": {
                            "uploadToken": upload_token.content.decode()
                        },
                    }
                ],
            },
            indent=4,
        )
        resp = session.post(
            "https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate",
            create_body,
        ).json()
        if "newMediaItemResults" in resp:
            return resp["newMediaItemResults"][0]["status"]
        try:
            del session.headers["Content-type"]
            del session.headers["X-Goog-Upload-Protocol"]
            del session.headers["X-Goog-Upload-File-Name"]
        except KeyError:
            pass

if __name__ == "__main__":
    from pymbbooth.api import JsApi
    session = setup_session()
    album_id = get_album_id(session, "Photobooth")
    api = JsApi()
    upload_photo(session, api.get_last_photo(), album_id)
