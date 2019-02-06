
import os
import getpass
import time
import sys
import cisco
import common as common


# Start Application
def StartGetInfo():
    f = open("host.txt")
    un = raw_input("Enter Username: ")
    pwd = getpass.getpass("Enter Password: ")
    for line in f:
        Task(line.strip(), un, pwd)


# Job Task
def Task(ipAddress, username, password):
    myClient = common.EstablishConn(ipAddress, username, password)
    if not myClient:
        return
    hostname = GetHostName(myClient)
    time.sleep(1)
    response = ApplyConf(myClient)
    common.WriteToFile(hostname+"_"+ipAddress, response)
    print ("*** Getting Information from Device " + hostname+" is Compelet ***")


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


def ApplyConf(client):
    file = open('shrun.txt')
    configurations = file.readlines()
    common.Print("Getting Information from Device")
    common.SendCommands(client, configurations)
    common.Loading(5, '', True)
    return client.recv(100000)
