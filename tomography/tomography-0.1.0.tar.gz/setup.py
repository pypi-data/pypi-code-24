from setuptools import setup, find_packages

setup(
    name="tomography",
    version="0.1.0",
    url="http://github.com/indexmotion/python-tomography/",
    author="indexmotion",
    author_email="indexmotion@gmail.com",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
)

