#!/bin/python3

from os import system
# clear group for safety
system("groupdel --force nopasswdlogin")
system("groupadd nopasswdlogin")

nopasswdloginusers = []

def auth(user):
	system("gpasswd -a " + user + " nopasswdlogin")
	global nopasswdloginusers
	nopasswdloginusers.append(user)

def deauth(user):
	system("gpasswd -d " + user + " nopasswdlogin")
	global nopasswdloginusers
	nopasswdloginusers.remove(user)

from os import listdir
from time import sleep
while True:
	for user in listdir("/home"):
		authed = False
		for application in open("/etc/ldmauth.conf").read().split("\n"):
			print("app:"+application.replace("$username", user))
			if "$username" not in application:
				#print("app:skip")
				continue
			if  system(application.replace("$username", user)) == 0:
				#print("app:sucess")
				authed = True
				break
			#else:
				#print("app:fail")
		if authed:
			auth(user)
		elif user in nopasswdloginusers:
			deauth(user)
	
	sleep(.8)
