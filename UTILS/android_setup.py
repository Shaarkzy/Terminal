#!/usr/bin/env python3
from os import system as sys

try:
    sys("pip install colorama")
    sys("pip install regex")
    sys("pip install tqdm")
    sys("pip install xdg")
    sys("pip install uuid")
    sys("pip install ipaddress")
    sys("pip install requests")
    sys("pip install psutil")
    sys("pip install netifaces")
    sys("pip install phonenumbers")
    sys("pip install pycryptodome")
    sys("pip install tenable-io")
    sys("pip install pytenable")
    sys("pip install scapy")
except:
    print ("\n[*] An error occured")

try:
    sys(f"chmod +x term.py; ln -s $(pwd)/term.py /data/data/com.termux/files/usr/bin/term")
    print ("\n[*] IF NOT ERROR: Start Terminal By executing: term")
except:
    print ("\n[*] An Error Occured")




