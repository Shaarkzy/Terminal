#Check For Supported OS
import platform as pt
pt = pt.system()
if pt != "Linux":
    print("[x]UNSUPPORTED OPERATING SYSTEM")
    quit(0)
else:
    pass

print("LOADING LIBRARIES")
def load_libraries():
    global sy, F, B, Sty, tm, socket, sub, rd, exists, os, re, uuid
    global ipaddress, r, json, tqdm, pt, p, phone, carrier, geocoder
    global timezone, AES, get_random_bytes, TenableIO, mimetypes
    global datetime, glob, sys, ifaddresses, interfaces
    global AF_INET, AF_INET6, n, readl, at

    import sys as sy
    print("━"*2, end="\r", flush=True)

    from colorama import Fore as F, Back as B, Style as Sty
    print("━"*4, end="\r", flush=True)

    import time as tm
    print("━"*6, end="\r", flush=True)

    import socket
    print("━"*8, end="\r", flush=True)

    import subprocess as sub
    print("━"*10, end="\r", flush=True)

    import random as rd
    print("━"*12, end="\r", flush=True)

    from os.path import exists
    print("━"*14, end="\r", flush=True)

    import os
    print("━"*16, end="\r", flush=True)

    import re
    print("━"*18, end="\r", flush=True)

    import uuid
    print("━"*20, end="\r", flush=True)

    import ipaddress
    print("━"*22, end="\r", flush=True)

    import requests as r
    print("━"*24, end="\r", flush=True)

    import json
    print("━"*26, end="\r", flush=True)

    from tqdm import tqdm
    print("━"*28, end="\r", flush=True)

    import platform as pt
    print("━"*30, end="\r", flush=True)

    import psutil as p
    print("━"*32, end="\r", flush=True)

    import phonenumbers as phone
    print("━"*34, end="\r", flush=True)

    from phonenumbers import carrier, geocoder, timezone
    print("━"*36, end="\r", flush=True)

    from Crypto.Cipher import AES
    print("━"*38, end="\r", flush=True)

    from Crypto.Random import get_random_bytes
    print("━"*40, end="\r", flush=True)

    from tenable.io import TenableIO
    print("━"*42, end="\r", flush=True)

    from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
    import netifaces as n
    print("━"*44, end="\r", flush=True)

    import mimetypes
    print("━"*46, end="\r", flush=True)

    from datetime import datetime
    print("━"*48, end="\r", flush=True)

    import glob
    print("━"*50, end="\r", flush=True)
    
    from os import system as sys
    print("━"*52, end="\r", flush=True)
    
    import readline as readl
    print("━"*54, end="\r", flush=True)
    
    import atexit as at
    print("━"*56, end="\r", flush=True)
    

__all__ = [
    "sy", "F", "B", "Sty", "tm", "socket", "sub", "rd", "exists", "os", "re", "uuid",
    "ipaddress", "r", "json", "tqdm", "pt", "p", "phone", "carrier", "geocoder", 
    "timezone", "AES", "get_random_bytes", "TenableIO", "interfaces", "ifaddresses", "AF_INET", "AF_INET6", "mimetypes", "datetime", "glob", "sys", "n", "readl", "at"
]
try:
    load_libraries()
except ModuleNotFoundError as er:
    print(er)
    quit(0)
