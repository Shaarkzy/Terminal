#!/bin/bash

git clone https://github.com/tenable/pytenable.git
cd pytenable; python3 setup.py build
python3 setup.py install
