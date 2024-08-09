#!/bin/bash

echo
echo 'INSTALLING AND BUILDING PYTENABLE.IO'
echo
pwd
git clone https://github.com/tenable/pytenable.git
cd pytenable; python3 setup.py build
python3 setup.py install
echo 
echo 'DONE'

