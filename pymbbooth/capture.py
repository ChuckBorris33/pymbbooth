import time
from datetime import datetime
from os import path
from PIL import Image
from io import BytesIO

from pymbbooth import config

try:
    import picamera

    has_picamera = True
except ImportError:
    has_picamera = False


def _prepare_countdown_image(number):
    img = Image.open(path.join(config.ASSETS_DIR, f"{number}.png"))
    padded = Image.new(
        "RGBA",
        (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ),
    )
    padded.paste(img, (0, 0))
    return padded


def prepare_countdown_images():
    return [_prepare_countdown_image(n) for n in range(5, 0, -1)]


def _add_overlay(camera, image):
    o = camera.add_overlay(image.tobytes(), size=image.size)
    o.alpha = 128
    o.layer = 3
    return o


def _save_photo(stream):
    stream.seek(0)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S%f")
    filename = f"image_{stamp}.jpg"
    image = Image.open(stream)
    image.save(path.join(config.PHOTO_DIR, filename))
    image.thumbnail((300, 300))
    image.save(path.join(config.THUBNAIL_DIR, filename))


def capture_photo(countdown_images):
    stream = BytesIO()
    # Max camera resolution 2592x1944
    if has_picamera:
        with picamera.PiCamera(
            resolution=config.CAPTURE_RESOLUTION, sensor_mode=config.CAPTURE_MODE
        ) as camera:
            camera.start_preview(resolution=config.PREVIEW_RESOLUTION)
            for image in countdown_images:
                overlay = _add_overlay(camera, image)
                time.sleep(1)
                camera.remove_overlay(overlay)
            camera.stop_preview()
            camera.capture(stream, format="jpeg")
            _save_photo(stream)
    else:
        print("Mocking capture")
        time.sleep(2)


if __name__ == "__main__":
    coundown_images = prepare_countdown_images()
    capture_photo(coundown_images)
