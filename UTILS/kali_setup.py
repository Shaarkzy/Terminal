#!/usr/bin/env python3
from os import system as sys

try:
    sys("apt-get install build-essential python3-dev")
    sys("apt-get install python3-colorama")
    sys("apt-get install python3-regex")
    sys("apt-get install python3-tqdm")
    sys("apt-get install python3-xdg")
    sys("apt-get install python3-uuid")
    sys("apt-get install python3-ipaddress")
    sys("apt-get install python3-requests")
    sys("apt-get install python3-psutil")
    sys("apt-get install python3-phonenumbers")
    sys("apt-get install python3-netifaces")
    sys("apt-get install python3-pycryptodome")
    sys("cd UTILS/LIB*; ./pycryptodome.sh")
    sys("cd UTILS/LIB*; ./pytenable.sh")
    sys("apt-get install python3-scapy")
except:
    print ("\n[*] An error occured")

try:
    sys(f"chmod +x term.py; ln -s $(pwd)/term.py /bin/term")
    print ("\n[*] IF NOT ERROR: Start Terminal By executing: term")
except:
    print ("\n[*] An Error Occured")




