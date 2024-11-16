#!/usr/bin/env python3
from os import system as sys

try:
    print("\nINSTALLING COLORAMA 1/12\n")
    sys("pip install colorama")
    print("\nDONE INSTALLING COLORAMA 1/12")

    print("\nINSTALLING REGEX 2/12\n")
    sys("pip install regex")
    print("\nDONE INSTALLING REGEX 2/12")

    print("\nINSTALLING TQDM 3/12\n")
    sys("pip install tqdm")
    print("\nDONE INSTALLING TQDM 3/12")

    print("\nINSTALLING XDG 4/12\n")
    sys("pip install xdg")
    print("\nDONE INSTALLING XDG 4/12")

    print("\nINSTALLING UUID 5/12\n")
    sys("pip install uuid")
    print("\nDONE INSTALLING UUID 5/12")

    print("\nINSTALLING IPADDRESSES 6/12\n")
    sys("pip install ipaddress")
    print("\nDONE INSTALLING IPADDRESS 6/12")

    print("\nINSTALLING REQUESTS 7/12\n")
    sys("pip install requests")
    print("\nDONE INSTALLING REQUESTS 7/12\n")

    print("\nINSTALLING PSUTILS 8/12\n")
    sys("pip install psutil")
    print("\nDONE INSTALLING PSUTILS 8/12")

    print("\nINSTALLING NETIFACES 9/12\n")
    sys("pip install netifaces")
    print("\nDONE INSTALLING NETIFACES 9/12\n")

    print("\nINSTALLING PHONENUMBERS 10/12\n")
    sys("pip install phonenumbers")
    print("\nDONE INSTALLING PHONENUMBERS 10/12")

    print("\nINSTALLING PYCRYPTODOME 11/12\n")
    sys("pip install pycryptodome")
    print("\nDONE INSTALLING PYCRYPTODOME 11/12")

    print("\nINSTALLING PYTENABLE 12/12\n")
    sys("pip install pytenable")
    print("\nDONE INSTALLING PYTENABLE 12/12")


except:
    print ("\n[*] Closed")

try:
    sys(f"chmod +x term.py; ln -s $(pwd)/term.py /data/data/com.termux/files/usr/bin/term")
    print ("\n[*] IF NOT ERROR: Start Terminal By executing: term")
except:
    print ("\n[*] Closed")




