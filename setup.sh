#!/bin/bash

echo 'Operating System: [android/kali] [1/2]: ' 
read user_input

if [ "$user_input" -eq 1 ]; then
    echo 'INSTALLING PYTHON3'
    pkg install python3
    echo 'DONE'
    ./UTILS/android_setup.sh
elif [ "$user_input" -eq 2 ]; then
    echo 'INSTALLING PYTHON3'
    apt-get install python3
    echo 'DONE'
    ./UTILS/kali_setup.sh
else
    echo 'INVALID INPUT'
fi
