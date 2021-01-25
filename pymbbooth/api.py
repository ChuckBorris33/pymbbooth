import glob
import os

from pymbbooth.capture import capture_photo, prepare_countdown_images
from pymbbooth.print import print_photo, job_state


def _get_ordered_files(path):
    files = glob.glob(path)
    files.sort(key=os.path.getmtime, reverse=True)
    return [os.path.basename(file) for file in files]


class JsAPi:
    PHOTO_PATH = os.path.abspath("public/photos/")

    def __init__(self):
        self.coundown_images = prepare_countdown_images()

    def get_last_photo(self):
        return _get_ordered_files(self.PHOTO_PATH + "/*.jpg")[0]

    def get_thumbnails(self):
        thumb_path = os.path.join(self.PHOTO_PATH, "thumbnails")
        return _get_ordered_files(thumb_path + "/*.jpg")

    def start_capture(self):
        return capture_photo(self.coundown_images)

    def print_photo(self, photo):
        return print_photo(photo)

    def job_state(self, job_id):
        return job_state(job_id)
