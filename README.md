# Shark Shell

Shell like emulator with utilities
Run Setup for libary installations and binary setup.
Program only for Linux.

**Run:**

```$ ./setup.sh ``` 

to build and configure program

**Program File Structure (Architecture)**
```Shell/
├── LICENSE
├── README.md
├── setup.sh
├── shell.py
├── __version__
├── UTILS/
│   ├── android_setup.sh
│   ├── kali_setup.sh
│   ├── .shell_history
│   ├── .shell_help
│   ├── check_os.py
│   ├── version.py
│   ├── resistor.py
│   ├── __pycache__
│   │       ├── check_os.cpython-312.pyc
│   │       └── version.cpython-312.pyc
│   └── BOOT_SETUP/
│       ├── pycryptodome.sh
│       ├── util_boot.py
│       └── __pycache__
│           └── util_boot.cpython-312.pyc
│       

```

**Note:**
```
1. Tested under Kali LInux Os and Android OS
2. Some utilities requires superuser privilege (on feature 10)...
3. For kali installation run setup as root
4. Program Folder must be in the home directory (~/Shell , /root/Shell)
```

**Features:**
```
1. Binary Tools
2. Port Scanner(multi/single)
3. File Management (Supports Cryptography)
4. Wifi Chat Room
5. File Transfer Via Wifi
6. Shell Host/Client
7. Weather Tools
8. Network Information
9. Cpu Information (might work without root access on earlier Android versions)
10. Mobile Number Osint(excluding personal information)
11. Grab Website Ip
12. Gather Information About An Ip Address.
13. File Searching
14. File and Folder Properties Viewer
```
**Good luck**
