#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written by RISHU KHAN
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo ="""
     \33[1;92m╔═══╗╔╗───╔═══╗╔═╗╔═╗
     \33[1;92m║╔═╗║║║───║╔══╝╚╗╚╝╔╝
     \33[1;92m║║─║║║║───║╚══╗─╚╗╔╝─
     \33[1;93m║╚═╝║║║─╔╗║╔══╝─╔╝╚╗─
     \33[1;92m║╔═╗║║╚═╝║║╚══╗╔╝╔╗╚╗ 
     \33[1;92m╚╝─╚╝╚═══╝╚═══╝╚═╝╚═╝
\33[1;92m-----------------------------------------------
\33[1;92m>> AUTHOR : RISHU KHAN
\33[1;92m>> FACEBOOK : RISHU
\33[1;92m>> YOUTUBE : NOI HAI
\33[1;92m-----------------------------------------------"""

                   
def main():
	os.system("clear")
	print(logo)
	print("")
	print(" \1b[1;92m    \Main menu")
	print("")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print(" \33[1;92m     [1] START CLONING\")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print("")
	os.system('xdg-open https://www.facebook.com/rishu.007')
	log_sel()
def log_sel():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		login()
	elif sel =="2":
		ran()
	
	else:
		print("")
		print("\Select valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \1b[1;91m  \Facebook login")
		print("")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print(" \1b[1;91m   [1] FACEBOOK ID/PASS LOGIN\")
		print(" \1b[1;92m   [2] FACEBOOK TOKEN LOGIN\")
		print("  \1b[1;91m  [3] Back ")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print("")
		log_select()
def log_select():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		ran()
	else:
		print("")
		print("\Select valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\Facebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("access_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\Account has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\Id/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\Login token")
        print("")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        token = raw_input        (" Paste token here: ")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
