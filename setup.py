#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="assistypes",
    version="1.0",
    description="My special types",
    author="Masynchin",
    author_email="masynchin@gmail.com",
    url="https://github.com/Masynchin/assistypes",
    packages=find_packages(exclude=["tests"]),
)
