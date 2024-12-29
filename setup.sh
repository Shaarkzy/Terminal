#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'

echo -e "${YELLOW}Operating System: [android/kali] [1/2]: ${NC}" 
read user_input

if [ "$user_input" -eq 1 ]; then
    echo -e "${GREEN}INSTALLING PYTHON3 ${NC}"
    pkg install python3
    echo -e "${BLUE}DONE${NC}"
    ./UTILS/android_setup.sh


elif [ "$user_input" -eq 2 ]; then
    echo -e "${GREEN}INSTALLING PYTHON3${NC}"
    apt-get install python3
    echo -e "${BLUE}DONE${NC}"
    ./UTILS/kali_setup.sh
else
    echo -e "${RED}INVALID INPUT${NC}"
fi
