#!/bin/bash

echo
echo 'INSTALLING AND BUILDING PYCRYPTODOME'
echo
git clone https://github.com/Legrandin/pycryptodome.git
pwd
cd pycryptodome; python3 setup.py build
python3 setup.py install
echo
echo 'DONE'
