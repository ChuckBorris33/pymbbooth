import glob
import os
import _thread

from pymbbooth.capture import capture_photo, prepare_countdown_images
from pymbbooth.print import print_photo, job_state
from pymbbooth.gphotos import setup_google_session, get_album_id, upload_photo
from pymbbooth import config


def _get_ordered_files(path):
    files = glob.glob(path)
    files.sort(key=os.path.getmtime, reverse=True)
    return [os.path.basename(file) for file in files]


class JsApi:
    def __init__(self):
        self.gsession = setup_google_session()
        self.album_id = get_album_id(self.gsession, config.ALBUM_NAME)
        self.coundown_images = prepare_countdown_images()

    def get_last_photo(self):
        
        return _get_ordered_files(config.PHOTO_DIR + "/*.jpg")[0]

    def get_thumbnails(self):
        return _get_ordered_files(config.THUBNAIL_DIR + "/*.jpg")

    def start_capture(self):
        photo_result =  capture_photo(self.coundown_images)
        _thread.start_new_thread(upload_photo, (self.gsession, self.get_last_photo(), self.album_id))
        return photo_result

    def print_photo(self, photo):
        return print_photo(photo)

    def job_state(self, job_id):
        return job_state(job_id)
