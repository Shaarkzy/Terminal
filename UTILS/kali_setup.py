#!/usr/bin/env python3
from os import system as sys

try:
    print("\nBUILDING ESSENTIALS FOR PYTHON3-DEV\n")
    sys("apt-get install build-essential python3-dev")
    print("\nDONE")

    print("\nINSTALLING COLORAMA 1/12\n")
    sys("apt-get install python3-colorama")
    print("\nDONE INSTALLING COLORAMA 1/12\n")

    print("\nINSTALLING REGEX 2/12\n")
    sys("apt-get install python3-regex")
    print("\nDONE INSTALLING REGEX 2/12\n")

    print("\nINSTALLING TQDM 3/12\n")
    sys("apt-get install python3-tqdm")
    print("\nDONE INSTALLING TQDM 3/12\n")

    print("\nINSTALLING XDG 4/12\n")
    sys("apt-get install python3-xdg")
    print("\nDONE INSTALLING XDG 4/12\n")

    print("\nINSTALLING UUID 5/12\n")
    sys("apt-get install python3-uuid")
    print("\nDONE INSTALLING UUID 5/12\n")

    print("\nINSTALLING IPADDRESS 6/12\n")
    sys("apt-get install python3-ipaddress")
    print("\nDONE INSTALLING IPADDRESS 6/12\n")

    print("\nINSTALLING REQUESTS 7/12\n")
    sys("apt-get install python3-requests")
    print("\nDONE INSTALLING REQUESTS 7/12\n")

    print("\nINSTALLING PSUTILS 8/12\n")
    sys("apt-get install python3-psutil")
    print("\nDONE INSTALLING PSUTILS 8/12\n")

    print("\nINSTALLING PHONENUMBERS 9/12\n")
    sys("apt-get install python3-phonenumbers")
    print("\nDONE INSTALLING PHONENUMBERS 9/12\n")

    print("\nINSTALLING NETIFACES 10/12\n")
    sys("apt-get install python3-netifaces")
    print("\nDONE INSTALLING NETIFACES 10/12\n")

    print("\nRUNNING SCRIPT FOR PYCRYPTODOME 11/12\n")
    sys("cd UTILS/LIB*; ./pycryptodome.sh")
    print("\nDONE INSTALLING PYCRYPTODOME 11/12\n")

    print("\nRUNNING SCRIPT FOR PYTENABLE  12/12\n")
    sys("cd UTILS/LIB*; ./pytenable.sh")
    print("\nDONE INSTALLING PYTENABLE 12/12\n")
except:
    print ("\n[*] Closed")

try:
    sys(f"chmod +x term.py; ln -s $(pwd)/term.py /bin/term")
    print ("\n[*] IF NOT ERROR: Start Terminal By executing: term")
except:
    print ("\n[*] Closed")




