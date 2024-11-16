#!/usr/bin/bash


echo -e "\nINSTALLING COLORAMA 1/12\n"
pip install colorama
echo -e "\nDONE INSTALLING COLORAMA 1/12"

echo -e "\nINSTALLING REGEX 2/12\n"
pip install regex
echo -e "\nDONE INSTALLING REGEX 2/12"

echo -e "\nINSTALLING TQDM 3/12\n"
pip install tqdm
echo -e "\nDONE INSTALLING TQDM 3/12"

echo -e "\nINSTALLING XDG 4/12\n"
pip install xdg
echo -e "\nDONE INSTALLING XDG 4/12"

echo -e "\nINSTALLING UUID 5/12\n"
pip install uuid
echo -e "\nDONE INSTALLING UUID 5/12"

echo -e "\nINSTALLING IPADDRESSES 6/12\n"
pip install ipaddress
echo -e "\nDONE INSTALLING IPADDRESSES 6/12"

echo -e "\nINSTALLING REQUESTS 7/12\n"
pip install requests
echo -e "\nDONE INSTALLING REQUESTS 7/12"

echo -e "\nINSTALLING PSUTILS 8/12\n"
pip install psutil
echo -e "\nDONE INSTALLING PSUTILS 8/12"

echo -e "\nINSTALLING NETIFACES 9/12\n"
pip install netifaces
echo -e "\nDONE INSTALLING NETIFACES 9/12"

echo -e "\nINSTALLING PHONENUMBERS 10/12\n"
pip install phonenumbers
echo -e "\nDONE INSTALLING PHONENUMBERS 10/12"

echo -e "\nINSTALLING PYCRYPTODOME 11/12\n"
pip install pycryptodome
echo -e "\nDONE INSTALLING PYCRYPTODOME 11/12"

echo -e "\nINSTALLING PYTENABLE 12/12\n"
pip install pytenable
echo -e "\nDONE INSTALLING PYTENABLE 12/12"

# Simulating "else" behavior
echo -e "\n[*] SETTING UP TERM.PY"
chmod +x term.py
ln -s "$(pwd)/term.py" /data/data/com.termux/files/usr/bin/term
echo -e "\n[*] IF NOT ERROR: Start Terminal By executing: term"



