import os
import paramiko
import getpass
import time
import sys
import socket
import cisco

''
#Start Application
def Start():
	introduction()
	f = open ("hostip.txt")
	un = "admin"
	pwd = "P@ssw0rd"
	for line in f:
		Task(line.strip(),un,pwd)
	

	
#Clear Screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')



#Introduction
def introduction():
	clear_screen()
	print '\n\n'
	print '\t#############################################################'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#         	      Cisco Automated tool       		         #'
	print '\t#                                                           #'
	print '\t#                      Beta Verion                          #'
	print '\t#                      Developed by Mohammed Abdelaal Ali   #'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#############################################################'
	print '\n\n\tPlease Press Enter to start\n\n'
	choice = raw_input('\n\n >> ')
	


#Job Task
def Task(ipAddress,username, password):
	myClient = EstablishConn(ipAddress,username,password)
	#print ("Accessing Device "+ ipAddress)
	time.sleep(1)
	response = ApplyConf(myClient)
	print ("*** Configuration had been applied "+ ipAddress+" ***")


#Establishing Connection
def EstablishConn(ip, username, password):
    sys.tracebacklimit = 0
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print ("---------- Connecting to Device: " + ip + " ----------")
    try:
        ssh_client.connect(hostname=ip, username=username,
                           password=password, port=5000)
        newConn = ()
        newConn = ssh_client.invoke_shell()
        print "susccfull connection", ip
        return newConn        
    except paramiko.SSHException:
        print '\t*** Authentication Failed ***'
        pass
    except socket.error:
        print '\t*** %s is Unreachable ***' % ip
        pass
    except Exception: 
        print 'Error found'
        pass   



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



#Configuration Commands
def commands():
	f = open ("conf.txt","r")
	lines = f.read().splitlines()
	f.close	
	print("\n".join(lines)) 
	return lines
'''


#Apply Configuration
def ApplyConf(client):
	file = open('conf.txt')
	configurations = file.readlines()
	#print ("Applying Configuration")
	cisco.helpers.Print('Apply Configuration')
	SendCommands(client,"conf t")
	for command in configurations:
		SendCommands(client, command.strip())
	#time.sleep(2)
	cisco.helpers.Loading(3,'',True)
	SaveConfig

#Save Configuration >>>>Not Working<<<<
def SaveConfig():
	SendCommands(client,"do wr mem \n")
	cisco.helpers.Print('Save Configuration')
	cisco.helpers.Loading(3,'',True)
	
       

#Type Commands
def SendCommands(client, message):
        #print message
        client.send(message)        
        client.send("\n")
       

'''

#Send Configuration Commands to Device
def Configure(client):
	cisco.helpers.Print('Apply Configuration')
	Send(client, "conf t \n")
	Send(client,commands())
	cisco.helpers.Loading(3,'',True)


#make gap between each command
def Send(client, messages):
	for x in range (len(messages)):
		client.send(messages[x])
		client.send("\n")
'''

Start()
