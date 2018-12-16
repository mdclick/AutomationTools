'''
Menu based Configuration

1- Apply Custome confirgua on Route
2- Apply Custome confit on ports by condition
    1- searching by CD{}
    2- Cisco AP
    3- Cisco IP Phone
3- Tpype cutomer valye

2- searching by Power
shwitchoort 
type poerr:15.3
Apply int 

woulr tlike toc y
3- getting infpormatio from youe
'''
import sys
import os
import paramiko
import getpass
import time
import cisco
import socket
import routerTools


def MainMenu():
    routerTools.common.Introduction()
    print ("     1. Apply Customize confgirauton on Router")
    print "\n"
    print ('2. Apply Configuration on Switch Ports by condition')
    print "\n"
    print ('3. Getting Infromation from Device')
    print '\n\n'

    choice=int(input("Enter your Choice:"))
    if choice==1:
        routerTools.ApplyConf.StartConf()
    if choice==2:
        #CDP()
        routerTools.ConfByPower.ConfByPower()
    if  choice==3:
        routerTools.GetInfo.StartGetInfo()
    #if choice==4:
    #   exit


MainMenu()
