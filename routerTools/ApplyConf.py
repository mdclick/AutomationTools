import os
import getpass
import time
import sys
import cisco
import common as common 


#Start Application
def StartConf():
	f = open ("host.txt")
	un = "admin"
	pwd = "P@ssw0rd"
	for line in f:
		Task(line.strip(),un,pwd)
	
#Job Task
def Task(ipAddress,username, password):
	myClient = common.EstablishConn(ipAddress,username,password)
	time.sleep(1)
	ApplyConf(myClient)
	print ("*** Configuration had been applied "+ ipAddress+" ***")



def ApplyConf(client):
	file = open('conf.txt')
	configurations = file.readlines()
	common.SendCommand(client,"conf t")
	common.Print("Apply Configuration")
	common.SendCommands(client, configurations)
	common.Loading(3,'',True)
	common.SaveConfig(client)
