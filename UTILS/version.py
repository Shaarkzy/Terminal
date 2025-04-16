
#------------------------------------------------------------------------------------------------------------------------------

import requests as req
from requests.exceptions import RequestException
import os
from .check_os import detect_os
import base64

#------------------------------------------------------------------------------------------------------------------------------

github_raw_version = "https://api.github.com/repos/Shaarkzy/Shell/contents/__version__?ref=main"

if detect_os:
    local_raw_version = '/data/data/com.termux/files/home/Shell/__version__'
else:
    user = sub.getoutput('whoami')
    local_raw_version = "/root/Shell/__version__" if os.geteuid() == 0 else '/home/{user}/Shell/__version__' 


#------------------------------------------------------------------------------------------------------------------------------




def get_github():
    try:
        response = req.get(github_raw_version, timeout=(3, 3))
        if response.status_code == 200: 
            file_cont = response.json()
            content = base64.b64decode(file_cont['content']).decode('utf-8')
            return content.strip()
        else:
            return False
    except RequestException:
        return False


#------------------------------------------------------------------------------------------------------------------------------



def get_local():
    open_file = open(local_raw_version, "r")
    return open_file.read().strip()

def check():
    check_git = get_github()
    check_local = get_local()

    
    if check_git != False:
        if check_git == check_local:
            return False
        else:
            return True
    else:
        return 'null_internet'


#------------------------------------------------------------------------------------------------------------------------------
#end line 61

