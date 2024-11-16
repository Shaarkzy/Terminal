#!/bin/bash

echo -e "\nBUILDING ESSENTIALS FOR PYTHON3-DEV\n"
apt-get install build-essential python3-dev
echo -e "\nDONE"

echo -e "\nINSTALLING COLORAMA 1/12\n"
apt-get install python3-colorama
echo -e "\nDONE INSTALLING COLORAMA 1/12\n"

echo -e "\nINSTALLING REGEX 2/12\n"
apt-get install python3-regex
echo -e "\nDONE INSTALLING REGEX 2/12\n"

echo -e "\nINSTALLING TQDM 3/12\n"
apt-get install python3-tqdm
echo -e "\nDONE INSTALLING TQDM 3/12\n"

echo -e "\nINSTALLING XDG 4/12\n"
apt-get install python3-xdg
echo -e "\nDONE INSTALLING XDG 4/12\n"

echo -e "\nINSTALLING UUID 5/12\n"
apt-get install python3-uuid
echo -e "\nDONE INSTALLING UUID 5/12\n"

echo -e "\nINSTALLING IPADDRESS 6/12\n"
apt-get install python3-ipaddress
echo -e "\nDONE INSTALLING IPADDRESS 6/12\n"

echo -e "\nINSTALLING REQUESTS 7/12\n"
apt-get install python3-requests
echo -e "\nDONE INSTALLING REQUESTS 7/12\n"

echo -e "\nINSTALLING PSUTILS 8/12\n"
apt-get install python3-psutil
echo -e "\nDONE INSTALLING PSUTILS 8/12\n"

echo -e "\nINSTALLING PHONENUMBERS 9/12\n"
apt-get install python3-phonenumbers
echo -e "\nDONE INSTALLING PHONENUMBERS 9/12\n"

echo -e "\nINSTALLING NETIFACES 10/12\n"
apt-get install python3-netifaces
echo -e "\nDONE INSTALLING NETIFACES 10/12\n"

echo -e "\nRUNNING SCRIPT FOR PYCRYPTODOME 11/12\n"
bash -c "cd UTILS/LIB* && ./pycryptodome.sh"
echo -e "\nDONE INSTALLING PYCRYPTODOME 11/12\n"

echo -e "\nRUNNING SCRIPT FOR PYTENABLE 12/12\n"
bash -c "cd UTILS/LIB* && ./pytenable.sh"
echo -e "\nDONE INSTALLING PYTENABLE 12/12\n"

echo -e "\n[*] SETTING UP TERM.PY"
chmod +x term.py
ln -s "$(pwd)/term.py" /bin/term
echo -e "\n[*] IF NOT ERROR: Start Terminal By executing: term"
