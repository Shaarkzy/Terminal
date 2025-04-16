#------------------------------------------------------------------------------------------------------------------------------

import subprocess as sub

#------------------------------------------------------------------------------------------------------------------------------

def detect_os():
     # Check for Kali
     kali_check = sub.getoutput("uname -a | grep -i kali").strip()
     if kali_check:
         return False
         
 
     # Check for Android
     android_check = sub.getoutput("uname -a | grep -i android").strip()
     if android_check:
         return True

#------------------------------------------------------------------------------------------------------------------------------
#end line 19
