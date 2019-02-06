
import os
import getpass
import time
import sys
import cisco
import common as common


def ConfByCDP():
    introduction()
    f = open("host.txt")
    un = raw_input("Enter Username: ")
    pwd = getpass.getpass("Enter Password")
    neighbor = raw_input("Type the Neighbor Name:")
    switches = f.readlines()
    for line in switches:
        CallRouter(line.strip(), un, pwd, neighbor)


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


def CallRouter(ipAddress, username, password, neighbor):
    myClient = common.EstablishConn(ipAddress, username, password)
    if not myClient:
        return
    router = cisco.Router(myClient)
    router.GetInterfacesByNeighbor()
    result = filter(lambda port: neighbor.lower()
                    in port.Neighbor.lower(), router.Interfaces)
    if len(result) > 0:
        print 'Found **', len(result), '** interfaces'
        for item in result:
            print "Platform: " + item.Neighbor
            print "Interface: " + item.Name
            print "============================="

        #input = raw_input("Would you like to configure, press[Y/y] ")
        # if(input.lower()== "y"):
        ApplyConf(myClient, result)


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
