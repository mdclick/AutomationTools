
import os
import paramiko
import getpass
import time
import cisco


def Start():
    introduction()
    f = open("hostip.txt")
    un = raw_input("Enter Username: ")
    pwd = getpass.getpass("Enter Password")
    for line in f:
        CallRouter(line.strip(), un, pwd)


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


def CallRouter(ipAddress, username, password):
    myClient = EstablishConn(ipAddress, username, password)
    router = cisco.Router(myClient)
    router.GetInterfacesByBreif()
    for port in router.Interfaces:
        print(port.Name, port.ip, port.Protocol, port.Status)


# Establishing Connection
def EstablishConn(ip, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print ("Connecting to Device: " + ip)
    try:
        ssh_client.connect(hostname=ip, username=username, password=password)
        print "susccfull connection", ip
    except paramiko.ssh_exception.SSHException:
        print '\t*** Authentication Failed ***'
    except socket.error:
        print '\t*** %s is Unreachable ***' % host

    newConn = ()
    newConn = ssh_client.invoke_shell()
    return newConn

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
