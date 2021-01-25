#!/usr/bin/env python
from subprocess import Popen

from watchgod import run_process
from watchgod.watcher import DefaultWatcher

from pymbbooth.app import run


class BoothWatcher(DefaultWatcher):
    def __init__(self, *args, **kwargs):
        self.ignored_dirs.update({"photos", "frontend"})
        super().__init__(*args, **kwargs)


def main():
    yarn = Popen(["yarn dev"], shell=True)
    try:
        run_process(
            path=".",
            target=run,
            kwargs={"develop": True},
            watcher_cls=BoothWatcher,
            callback=lambda f: print("Reloading app..."),
        )
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        yarn.terminate()


if __name__ == "__main__":
    main()
