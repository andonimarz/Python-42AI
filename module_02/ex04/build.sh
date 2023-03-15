#!/bin/bash

# Update pip
pip install --upgrade pip

# Build distribution packages in wheel format
python setup.py bdist_wheel

# Build distribution packages in tar.gz format
python setup.py sdist
