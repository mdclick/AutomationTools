import sys
import os
import paramiko
import getpass
import time
import cisco
import socket
import routerTools


def MainMenu():
    routerTools.common.MainIntroduction()
    print ("     1. Apply Confgirauton on Device")
    print "\n"
    print ('     2. Apply Configuration on Switch Port by condition')
    print "\n"
    print ('     3. Getting Infromation from Device')
    print "\n"
    print ('     0. Exit')
    print "\n"

    print '\n\n'

    Achoice = int(input("Enter your choice:"))
    if Achoice == 1:
        routerTools.ApplyConf.StartConf()
    if Achoice == 2:
        routerTools.common.SubIntroduction()
        print "\n"
        print "\n"
        print ('     1. Filter By CDP')
        print "\n"
        print ('     2. Filter By Power')
        print "\n"
        print ('     3. Back')
        print '\n\n'
        Bchoice = int(input("Enter your choice:"))
        if Bchoice == 1:
            print '\n\n'
            routerTools.ConfByCDP.ConfByCDP()
        if Bchoice == 2:
            print '\n\n'
            routerTools.ConfByPower.ConfByPower()
        if Bchoice == 3:
            print '\n\n'
            MainMenu()

    elif Achoice == 3:
        print '\n\n'
        routerTools.GetInfo.StartGetInfo()
    elif Achoice == 0:
        sys.exit
    else:
        print ('     Invalid choice')
        MainMenu()


MainMenu()
