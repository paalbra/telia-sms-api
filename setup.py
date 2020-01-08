import os.path

import setuptools

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setuptools.setup(
    name="telia-sms-api",
    version="0.1",
    description="Simple API tool for the Telia SMS webservice",
    install_requires=[
        "requests",
    ],
    py_modules=[
        "telia"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Paal Braathen",
    author_email="paalbra@gmail.com",
    url="https://github.com/paalbra/telia-sms-api"
)
