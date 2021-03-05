from setuptools import setup, find_packages
import pathlib
import os


def tree(src):
    return [
        (root, map(lambda f: os.path.join(root, f), files))
        for (root, dirs, files) in os.walk(os.path.normpath(src))
    ]


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    app="pymbbooth/app.py",
    name="pymbbooth",
    version="0.0.1",
    description="Raspberry pie photobooth app",
    long_description=long_description,  # from readme
    long_description_content_type="text/markdown",
    # url='https://github.com/pypa/sampleproject', # link to github
    author="Boris Zalman",
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="boris.zalman33@gmail.com",  # Optional
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Raspberry pie :: Photography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="raspberry, photobooth",
    python_requires=">=3.7, <4",
    install_requires=["Pillow", "pywebview[gtk]", "picamera", "pycups"],
    data_files=tree("public"),
    entry_points={
        "console_scripts": [
            "photobooth=pymbbooth.app:run",
        ],
    },
)
