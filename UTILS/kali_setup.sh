#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo -e "\n${BLUE}BUILDING ESSENTIALS FOR PYTHON3-DEV${NC}\n"
apt-get install build-essential python3-dev
echo -e "\n${BLUE}DONE${NC}\n"

echo -e "\n${GREEN}INSTALLING COLORAMA 1/13${NC}\n"
apt-get install python3-colorama
echo -e "\n${GREEN}DONE INSTALLING COLORAMA 1/13${NC}\n"

echo -e "\n${YELLOW}INSTALLING REGEX 2/13${NC}\n"
apt-get install python3-regex
echo -e "\n${YELLOW}DONE INSTALLING REGEX 2/13${NC}\n"

echo -e "\n${BLUE}INSTALLING TQDM 3/13${NC}\n"
apt-get install python3-tqdm
echo -e "\n${BLUE}DONE INSTALLING TQDM 3/13${NC}\n"

echo -e "\n${GREEN}INSTALLING XDG 4/13${NC}\n"
apt-get install python3-xdg
echo -e "\n${GREEN}DONE INSTALLING XDG 4/13${NC}\n"

echo -e "\n${YELLOW}INSTALLING UUID 5/13${NC}\n"
apt-get install python3-uuid
echo -e "\n${YELLOW}DONE INSTALLING UUID 5/13${NC}\n"

echo -e "\n${BLUE}INSTALLING IPADDRESS 6/13${NC}\n"
apt-get install python3-ipaddress
echo -e "\n${BLUE}DONE INSTALLING IPADDRESS 6/13${NC}\n"

echo -e "\n${GREEN}INSTALLING REQUESTS 7/13${NC}\n"
apt-get install python3-requests
echo -e "\n${GREEN}DONE INSTALLING REQUESTS 7/13${NC}\n"

echo -e "\n${YELLOW}INSTALLING PSUTILS 8/13${NC}\n"
apt-get install python3-psutil
echo -e "\n${YELLOW}DONE INSTALLING PSUTILS 8/13${NC}\n"

echo -e "\n${BLUE}INSTALLING PHONENUMBERS 9/13${NC}\n"
apt-get install python3-phonenumbers
echo -e "\n${BLUE}DONE INSTALLING PHONENUMBERS 9/13${NC}\n"

echo -e "\n${GREEN}INSTALLING NETIFACES 10/13${NC}\n"
apt-get install python3-netifaces
echo -e "\n${GREEN}DONE INSTALLING NETIFACES 10/13${NC}\n"

echo -e "\n${YELLOW}RUNNING SCRIPT FOR PYCRYPTODOME 11/13${NC}\n"
bash -c "cd UTILS/LIB* && ./pycryptodome.sh"
echo -e "\n${YELLOW}DONE INSTALLING PYCRYPTODOME 11/13${NC}\n"

echo -e "\n${BLUE}RUNNING SCRIPT FOR PYTENABLE 12/13${NC}\n"
bash -c "cd UTILS/LIB* && ./pytenable.sh"
echo -e "\n${BLUE}DONE INSTALLING PYTENABLE 12/13${NC}\n"

echo -e "\n${BLUE}INSTALLING NEOFETCH 13/13${NC}\n"
apt-get install neofetch
echo -e "\n${BLUE}DONE INSTALLING NEOFETCH 13/13${NC}\n"

echo -e "\n${GREEN}[*] SETTING UP TERM.PY${NC}"
chmod +x term.py
ln -s "$(pwd)/term.py" /bin/term
echo -e "\n${YELLOW}[*] IF NOT ERROR: Start Terminal By executing: term${NC}\n"
