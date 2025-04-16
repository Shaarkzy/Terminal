#!/bin/bash

git clone https://github.com/Legrandin/pycryptodome.git
cd pycryptodome; pip install --upgrade pip setuptools wheel; pip install .
