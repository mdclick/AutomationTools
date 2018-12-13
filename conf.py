import os
import paramiko
import getpass
import time
import sys
import socket
import cisco

''
def Start():
	introduction()
	f = open ("hostip.txt")
	un = raw_input("Enter Username: ")
	pwd = getpass.getpass("Enter Password: ")
	for line in f:
		Task(line.strip(),un,pwd)
	

	

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')




#Introduction
def introduction():
	clear_screen()
	print '\n\n'
	print '\t#############################################################'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#            Welcome to Cisco Beta Automated tool           #'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#                      Developed by Mohammed Abdelaal Ali   #'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#############################################################'
	print '\n\n\tPlease Press Enter to start\n\n'
	choice = raw_input('\n\n >> ')
	



#Job Task
def Task(ipAddress,username, password):
	myClient = EstablishConn(ipAddress,username,password)
	print ("Accessing Device "+ ipAddress)
	time.sleep(1)
	response = Configure(myClient)
	print ("*** Configuration had been applied "+ ipAddress+" ***")

#Establishing Connection
def EstablishConn(ip,username,password):
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print ("---------- Connecting to Device: " + ip + " ----------")
	try:
		ssh_client.connect(hostname=ip,username=username,password=password)
		print "susccfull connection", ip
	except paramiko.ssh_exception.SSHException:
		print '\t*** Authentication Failed ***'
	except socket.error:
		print '\t*** %s is Unreachable ***' % host

	newConn= ()
	newConn = ssh_client.invoke_shell()
	return newConn
'''
#Getting match input
def GetPower (connection):
	connection.send("ter len 0\n")
	connection.send("sh power inline | i 30.0\n")
	time.sleep(3)
	res = connection.recv(50000)
	lines = res.split("\n")
	host="hostname"
	hostNameLine = next((value for value in lines if value is not None and value.lower().startswith(host.lower())),None)
	hostName = hostNameLine.split()[1]
	return hostName
'''
#Configuration Commands
def commands():
	f = open ("conf.txt","r")
	lines = f.read().splitlines()
	f.close	
	#print("\n".join(lines)) 
	return lines

#Send Configuration Commands to Device
def Configure(client):
	cisco.helpers.Print('Apply Configuration')
	Send(client,commands())
	cisco.helpers.Loading(3,'',True)


#make gap between each command
def Send(sender, messages):
	for x in range (len(messages)):
		sender.send(messages[x])
		sender.send("\n")
	

Start()
