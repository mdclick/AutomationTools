
import sys
import os
import paramiko
import getpass
import time
import cisco
import socket


def Start():
    introduction()
    f = open("hostip.txt")
    un = "admin"
    pwd = "P@ssw0rd"
    power = raw_input("Input the power: ")
    switches = f.readlines()
    for line in switches:
        CallRouter(line.strip(), un, pwd, power)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Introduction
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
    raw_input('\n\n >> ')


def CallRouter(ipAddress, username, password, power):
    myClient = EstablishConn(ipAddress, username, password)
    if not myClient:
        return 
    router = cisco.Router(myClient)
    router.GetInterfacesByPower()
    result = filter(lambda port: port.Power == float(power) and port.Admin == cisco.InterfaceAdmin.Auto, router.Interfaces)
    for item in result:
        print item.Name
    '''
    input = raw_input("Would you like to configure, press[Y/y] ")
    if(input.lower()== "y"):
    '''
    ApplyConf(myClient, result)



def ApplyConf(sender, ports):
    file = open('conf.txt')
    configurations = file.readlines()
    for port in ports:
        print "Configuring ", port.Name, "...."
        SendCommands(sender,"conf t")
        SendCommands(sender,"defau "+port.Name)
        time.sleep(2)
        SendCommands(sender,"int "+port.Name)
        for command in configurations:
            SendCommands(sender, command.strip())
        time.sleep(3)
       

    # Establishing Connection
def SendCommands(sender, message):  
        # print message
        sender.send(message)        
        sender.send("\n")

def EstablishConn(ip, username, password):
    sys.tracebacklimit = 0
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print ("Connecting to Device: " + ip)
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

# Job Task


'''
def Task(ipAddress, username, password):
    myClient = EstablishConn(ipAddress, username, password)
    hostname = GetHostName(myClient)
    print ("Getting the following Information from Device " + ipAddress)
    time.sleep(1)
    response = ShowInfo(myClient)
    WriteToFile(hostname+"_"+ipAddress, response)
    print ("*** Getting Information from Device " + hostname+" is Compelet ***")


# Getting Hostname
def GetHostName(connection):
    connection.send("ter len 0\n")
    connection.send("sh run | i hostname\n")
    time.sleep(3)
    res = connection.recv(50000)
    lines = res.split("\n")
    host = "hostname"
    hostNameLine = next((value for value in lines if value is not None and value.lower(
    ).startswith(host.lower())), None)
    hostName = hostNameLine.split()[1]
    return hostName


# list of Show Commands
def commands():
    f = open("shrun.txt", "r")
    lines = f.read().splitlines()
    f.close
    print("\n".join(lines))
    return lines


# Send Show information Commands to Device
def ShowInfo(client):
    Send(client, commands())
    time.sleep(5)
    return client.recv(50000)


# make gap between each command
def Send(sender, messages):
    for x in range(len(messages)):
        for number in range(0, 5):
            sender.send("\n")
        sender.send(messages[x])
        sender.send("\n")


# Save Output to file
def WriteToFile(fileName, message):
    file = open(fileName+'.txt', 'w')
    file.write(message)
    file.close()

'''
Start()
