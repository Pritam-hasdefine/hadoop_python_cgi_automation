import subprocess
import getpass
import os
#subprocess.getstatusoutput("tput setaf 1")           sometimes won't work
os.system("tput setaf 1")
choice="y"
print("\t\tWelcome to the menu!!!\n\t-----------------------------------------")
os.system("tput setaf 0") 
print("""
Where you want to run the command?
1.Local System
2.Remote System
""")
r=int(input("Enter your choice:"))
if r==2:
	ip=input("Enter IP address:")
	y=getpass.getpass("Enter password:")
while choice=="y" or choice=="Y" :
	if r==1 :
		print( """
		Press 1: Date
		Press 2: CAl
		Press 3: user creation
		Press 4: file creation
		Press 5: Web server
		Press 6: Exit
		""")
		x=int(input("Enter your choice:"))
		if x==1 :
			com=subprocess.getstatusoutput("date")
			if com[0]==0:
				print(com[1])
				continue
			else:
				print("Sorry. Command cannot be executed!")
				continue
		elif x==2 :
			com=subprocess.getstatusoutput("cal")
			if com[0]==0:
				print(com[1])
				continue
			else:
				print("Sorry. Command cannot be executed!")
				continue
		elif x==3 :
			x=input("Enter the name of user:")
			com=subprocess.getstatusoutput("useradd {}".format(x))		
			if com[0] != 0:
				print("User exists")
				continue
			else:
				y=getpass.getpass("Enter password:")		
				com2=subprocess.getstatusoutput("echo {} | passwd {} --stdin".format(y,x))
				if com2[0]==0:
					print("User added")
					continue
				else:
					subprocess.getstatusoutput("userdel {}".format(x))
					print("Error in providing password!")
					continue
		elif x==4:
			f=input("Enter the name of file:")
			com=subprocess.getstatusoutput('touch {}'.format(f))
			if com[0]==0:
				print("File created")
				continue
			else:
				print("Failed to create file!!!")
				continue
		elif x==5:
			com=subprocess.getstatusoutput("yum install httpd -y")
			if com[0] != 0:
				print("Error in installing http server!")
				continue
			else:
				doc=input("Enter the name of html document to load (full name):")
				com=subprocess.getstatusoutput("cp {} /var/www/html".format(doc))
				if com[0] == 0:
					com2=subprocess.getstatusoutput("systemctl restart httpd")
					if com2[0] != 0:
						print("Error in restarting http server!")
						continue
				else: 
					print("Cannot load file")
					continue
				print("File uploaded on server successfully")			
				continue
		elif x==6:
			print("Exiting.")
			exit()
		
		else :
			print("Wrong choice")
		input("Press enter to continue:")
		os.system("clear")
		
	elif r==2: 
		print( """
		Press 1: Date
		Press 2: CAl
		Press 3: user creation
		Press 4: file creation
		Press 5: Web server
		Press 6: Exit
		""")
		x=int(input("Enter your choice:"))
		if x==1 :
			com=subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} date".format(y,ip))
			if com[0]==0:
				print(com[1])
				continue
			else:
				print("Sorry. Command cannot be executed!")
				continue
		elif x==2 :
			com=subprocess.getstatusoutput("sshpass -p {} ssh -l root -o StrictHostKeyChecking=no {} cal".format(y,ip))
			if com[0]==0:
				print(com[1])
				continue
			else:
				print("Sorry. Command cannot be executed!")
				continue
		elif x==3 :
			x=input("Enter the name of user:")
			com=subprocess.getstatusoutput("sshpass -p {} ssh -l root -o StrictHostKeyChecking=no {} useradd {}".format(y,ip,x))		
			if com[0] != 0:
				print("User exists")
				continue
			else:
				p=getpass.getpass("Enter password:")		
				com2=subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} echo {} | passwd {} --stdin".format(y,ip,p,x))
				if com2[0]==0:
					print("User added")
					continue
				else:
					subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} userdel {}".format(y,ip,x))
					print("Error in providing password!")
					continue
		elif x==4:
			f=input("Enter the name of file:")
			com=subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} touch {}".format(y,ip,f))
			if com[0]==0:
				print("File created")
				continue
			else:
				print("Failed to create file!!!")
				continue
		elif x==5:
			com=subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} yum install httpd -y".format(y,ip))
			if com[0] != 0:
				print("Error in installing http server!")
				continue
			else:
				doc=input("Enter the name of html document to load (full name):")
				com=subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} cp {} /var/www/html".format(y,ip,doc))
				if com[0] == 0:
					com2=subprocess.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} systemctl restart httpd".format(y,ip))
					if com2[0] != 0:
						print("Error in restarting http server!")
						continue
				else: 
					print("Server configured.Cannot load file!")
					continue
				print("File uploaded on server successfully")			
				continue
		elif x==6:
			print("Exiting.")
			exit()
		
		else :
			print("Wrong choice")
		input("Press enter to continue:")
		subprocess.getstatusoutput("clear")
	choice=input("Want to continue(y/n)")
	if choice=="N" or choice=="n":
		exit()
 
