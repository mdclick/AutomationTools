import os
import getpass
import time
import sys
import cisco
import common as common


def ConfByPower():
    f = open("host.txt")
    un = raw_input("Enter Username: ")
    pwd = getpass.getpass("Enter Password: ")
    ok = False
    while not ok:
        power = raw_input("Enter Power value:")
        try:
            power = float(power)
            ok = True
        except ValueError:
            print('Input value is not correct !')
    switches = f.readlines()
    for line in switches:
        CallRouter(line.strip(), un, pwd, power)


def CallRouter(ipAddress, username, password, power):
    myClient = common.EstablishConn(ipAddress, username, password)
    if not myClient:
        return
    router = cisco.Router(myClient)
    router.GetInterfacesByPower()
    result = filter(lambda port: port.Power == float(
        power) and port.Admin == cisco.InterfaceAdmin.Auto, router.Interfaces)
    if len(result) > 0:
        print 'Found **', len(result), '** interfaces'
        ApplyConf(myClient, result)
    else:
        print "No matched Device !"
    '''
    input = raw_input("Would you like to configure, press[Y/y] ")
    if(input.lower()== "y"):
    '''


def ApplyConf(client, ports):
    common.SendCommand(client, "conf t")
    file = open('switchport.txt')
    configurations = file.readlines()
    for port in ports:
        common.Print("Configuring " + port.Name)
        common.SendCommand(client, "default int "+port.Name)
        common.Loading(1)
        common.SendCommand(client, "int "+port.Name)
        common.SendCommands(client, configurations)
        common.Loading(2)
        print('')
    common.SaveConfig(client)
