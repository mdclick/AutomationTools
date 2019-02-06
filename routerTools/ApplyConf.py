import os
import getpass
import time
import sys
import cisco
import common as common


# Start Application
def StartConf():
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
    time.sleep(1)
    ApplyConf(myClient)
    print ("*** Configuration had been applied " + ipAddress+" ***")


def ApplyConf(client):
    file = open('conf.txt')
    configurations = file.readlines()
    common.SendCommand(client, "conf t")
    common.Print("Apply Configuration")
    common.SendCommands(client, configurations)
    common.Loading(3, '', True)
    common.SaveConfig(client)
