import os
import getpass
import time
import sys
import cisco
import common as common 


def ConfByPower():
    f = open("host.txt")
    un = raw_input("Enter Username: ")
    pwd = getpass.getpass("Enter Password")
    power = raw_input("Input the power: ")
    switches = f.readlines()
    for line in switches:
        CallRouter(line.strip(), un, pwd, power)


def CallRouter(ipAddress, username, password, power):
    myClient = common.EstablishConn(ipAddress, username, password)
    if not myClient:
        return 
    router = cisco.Router(myClient)
    router.GetInterfacesByPower()
    result = filter(lambda port: port.Power == float(power) and port.Admin == cisco.InterfaceAdmin.Auto, router.Interfaces)
    if len(result)>0:
        print 'Found' , len(result), 'interfaces'
        ApplyConf(myClient, result)
    
    '''
    input = raw_input("Would you like to configure, press[Y/y] ")
    if(input.lower()== "y"):
    '''
    


def ApplyConf(client, ports):
    file = open('conf.txt')
    configurations = file.readlines()
    for port in ports:
        common.Print("Configuring " + port.Name)
        common.SendCommands(client,"conf t")
        common.SendCommands(client,"defau "+port.Name)
        common.Loading(1)
        common.SendCommands(client,"int "+port.Name)
        for command in configurations:
            common.SendCommands(client, command.strip())
        common.Loading(2)
        print('')
    common.SaveConfig(client)