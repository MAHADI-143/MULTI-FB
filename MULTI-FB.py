import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from MULTI64 import login_main
 
        login_main()
 
 
 
elif bit == "32bit":
 
        from ML32 import login_main
 
 
        login_main()
