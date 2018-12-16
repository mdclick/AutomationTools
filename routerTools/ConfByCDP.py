
import os
import getpass
import time
import sys
import cisco
import common as common 


def ConfByPower():
    introduction()
    f = open("host.txt")
    un = raw_input("Enter Username: ")
    pwd = getpass.getpass("Enter Password")
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
    myClient = common.EstablishConn(ipAddress, username, password)
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



def ApplyConf(client, ports):
    file = open('conf.txt')
    configurations = file.readlines()
    for port in ports:
        print "Configuring ", port.Name, "...."
        common.SendCommands(client,"conf t")
        common.SendCommands(client,"defau "+port.Name)
        time.sleep(1)
        common.SendCommands(client,"int "+port.Name)
        for command in configurations:
            common.SendCommands(client, command.strip())
        time.sleep(2)
    common.SendCommand(client,"do wr mem")
    print ("Save Configuration ...")
    time.sleep(3)