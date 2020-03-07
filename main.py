#!/usr/bin/python36
print("content-type:text/html")
print("\n")

import subprocess
import os
import cgi

data=cgi.FieldStorage()
x=data.getvalue('command')
if x=="1" :
	print(subprocess.getoutput("date"))
elif x=="2" :
	print(subprocess.getoutput("cal"))
elif x=="4" :
	x=input("Enter the name of user:")
	subprocess.getoutput("useradd "+x)		#two types of formatting
	if (os.system("echo $?")!=0) :
		print("User exists")
	else:
		y=input("Enter password:")		
		subprocess.getoutput("echo {} | passwd {} --stdin".format(y,x))
		print("User added")
			
elif x=="3":
	f=input("Enter the name of file:")
	subprocess.getoutput("touch "+f)
	if(os.system("echo $?")==0):
		print("File created")
elif x=="5":
	os.system("yum install httpd -y")
	if os.system("echo $?") != 0:
		print("Error in installing http server!")
		exit()#continue
	else:	
		doc=input("Enter the name of html document(to load):")
		os.system("cp {} /var/www/html".format(doc))
		if os.system("echo $?") == 0:
			os.system("systemctl restart httpd")
			if os.system("echo $?") != 0:
				print("Error in restarting http server!")
				exit()#continue
		else: 
			print("Cannot load file")
			exit()#continue
	print("File uploaded on server successfully")

			#content=input("Enter the content:")
			#os.system("gedit {}".format(doc.html))
			#if (os.system("echo $!")==0):
			
			
elif x=="7":
	print("Exiting.")
	exit()
else :
	print("Wrong input.")
	exit()
