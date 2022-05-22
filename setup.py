# -*- coding: utf-8 -*-
# experimental setup py
import sys

from setuptools import find_packages, setup

VERSION_SUFFIX = "%d.%d" % sys.version_info[:2]


with open("README.rst") as readme:
    long_description = readme.read()


dependencies = [
    "sacred",
    "https://github.com/tagucci/pythonrouge"
]

if VERSION_SUFFIX == "3.4":  # lxml 4.4.0 dropped support for Python 3.4
    dependencies.append("lxml<4.4.0")

setup(
    name="sumy",
    version="0.10.0",
    description="Module for automatic summarization of text documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="M Adib",
    author_email="adib35785@gmail.com",
    url="https://github.com/adib-enc/indosum",
    license="Apache License, Version 2.0",
    keywords=[
        "data mining",
        "automatic summarization",
        "data reduction",
        "web-data extraction",
        "NLP",
        "natural language processing",
        "TextRank",
        "LexRank",
    ],
    install_requires=dependencies,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",

        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Czech",
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: German",
        "Natural Language :: Hebrew",
        "Natural Language :: Italian",
        "Natural Language :: Japanese",
        "Natural Language :: Portuguese",
        "Natural Language :: Slovak",
        "Natural Language :: Spanish",
        "Natural Language :: Ukrainian",
        "Natural Language :: Greek",

        "Topic :: Education",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Linguistic",

        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)