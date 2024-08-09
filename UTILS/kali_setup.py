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
    sys("apt-get install python3-pycryptodome")
    sys("cd UTILS/LIB*; ./pycryptodome.sh")
    sys("cd UTILS/LIB*; ./pytenable.sh")
    sys("apt-get install python3-scapy")
except:
    print ("[*] An error occured")

print('\n\nExample: /my/directory/to/term.py & /my/directory/to/bin\n\n')

path_to_pro = input("[*]::'/path/to/term.py': ")
path_to_bin = input("[*]::'/path/to/bin': ")

try:
    sys(f"chmod +x {path_to_pro}")
    sys(f"ln -s {path_to_pro} {path_to_bin}/term")
    print ("[*] IF NOT ERROR: Start Terminal By executing: 'term'")
except:
    print ("[*] An Error Occured")




