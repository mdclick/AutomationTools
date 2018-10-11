import os
import paramiko
import time

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def Start():
	introduction()
	lines = open ("switch.txt")
	username = raw_input("Enter Username:  ")
	password = getpass.getpass(prompt="Enter Password: ")
	for line in lines:
		Task(line.strip(),username,password)


def introduction():
	clear_screen()
	print '\n\n'
	print '\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
	print '\t*                                                           *'
	print '\t*                                                           *'
	print '\t*   Welcome to Beta Automated tool                          *'
	print '\t*                                                           *'
	print '\t*                                                           *'
	print '\t*                      Developed by Mohammad Mahmoud        *'
	print '\t*                                                           *'
	print '\t*                                                           *'
	print '\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
	print '\n\n\tPlease Press Enter to start\n\n'
	choice = raw_input('\n\n >> ')



def Task(ipAddress,username, password):
	myClient = EstablishConn(ipAddress,username,password)
	hostname = GetHostName(myClient)
	print ("Getting the following Information from Device "+ ipAddress)
	response = ShowInfo(myClient)
	WriteToFile(hostname+"_"+ipAddress,response)
	print ("*** Getting Information from Device "+ hostname+" is Compelet ***")


def EstablishConn(ip,username,password):
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print ("Connecting to Device: " + ip)
	ssh_client.connect(hostname=ip,username=username,password=password)
	print "susccfull connection", ip
	newConn= ()
	newConn = ssh_client.invoke_shell()
	return newConn

def GetHostName (connection):
	connection.send("sh run | i hostname\n")
	time.sleep(3)
	res = connection.recv(50000)
	lines = res.split("\n")
	host="hostname"
	hostNameLine = next((value for value in lines if value is not None and value.lower().startswith(host.lower())),None)
	hostName = hostNameLine.split()[1]
	return hostName


def commands():
	f = open ("shrun.txt","r")
	lines = f.read().splitlines()
	f.close	
	print("\n".join(lines)) 
	return lines


def ShowInfo(client):
	Send(client,commands())
	time.sleep(1)
	return client.recv(50000)

def Send(sender, messages):
	for n in range (0,5):
		sender.send("\n")
	for x in range (len(messages)):
		sender.send(messages[x])
		sender.send("\n")
	

def WriteToFile(fileName, message):
	file = open(fileName+'.txt', 'w')
	file.write(message)
	file.close() 


Start()
