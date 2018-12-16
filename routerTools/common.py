import os
import paramiko
import getpass
import time
import sys
import socket
import cisco


#Clear Screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


#Introduction
def Introduction():
	clear_screen()
	print '\n\n'
	print '\t#############################################################'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#         	      Cisco Automated tool                  #'
	print '\t#                                                           #'
	print '\t#                      Beta Verion                          #'
	print '\t#                      Developed by Mohammed Mahmoud        #'
	print '\t#                                                           #'
	print '\t#                                                           #'
	print '\t#############################################################'
	print '\n\n\tPlease Press Enter to start\n\n'
	raw_input('\n\n >> ')


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
        print "Susccfull Connection", ip
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

#Type Commands
def SendCommand(client, message):
        client.send(message)        
        client.send("\n")

#Send Command
def SendCommands(client, messages):
    for msg in messages:
        SendCommand(client,msg)

def Print(msg, newLine=False):
        sys.stdout.write(msg)
        sys.stdout.flush()
        if(newLine):
                Print('\n')


def SaveConfig(client):
	SendCommand(client,"do wr mem")
	Print('Save Configuration')
	Loading(3,'',True)       



#Save Output to file
def WriteToFile(fileName, message):
	file = open(fileName+'.txt', 'w')
	file.write(message)
	file.close() 



def Loading(seconds, msg='', newLine=False):
    x = 0
    sys.stdout.write(msg)
    while x<seconds:
        time.sleep(1)
        Print('.')       
        x+=1
    if(newLine):
        Print('\n')
