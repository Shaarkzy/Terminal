#!/bin/bash

git clone https://github.com/Legrandin/pycryptodome.git;
cd pycryptodome;
python3 setup.py build;
python3 setup.py install
