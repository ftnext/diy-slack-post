from setuptools import setup, find_packages


setup(
    name="postslack",
    version="0.1",
    packages=find_packages(exclude=["tests.*", "tests"]),
)
