import os
import argparse

import webview

from pymbbooth.api import JsAPi

INDEX_PATH = os.path.abspath("public/index.html")


def run(develop=False):
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--develop", default=develop)
    arguments = parser.parse_args()

    try:
        window = webview.create_window(
            "Photobooth", INDEX_PATH, fullscreen=True, frameless=False, js_api=JsAPi()
        )
        webview.start(http_server=True, debug=arguments.develop)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    run()
