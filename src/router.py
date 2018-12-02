import paramiko
import time
from interface import *


class Router:
    Interfaces = []

    def __init__(self, client):
        self.client = client

    def getInterfacesByPower(self):
        result = self.Send(["terminal length 0", "show power inline"])
        values = result.splitlines()
        for(value in values):
            if(value.lower.startsWith('gi', 'fa', 'te')):
                Interfaces.append(
                    Interface.FromPower(value[0], value[1], value[2], value[3]))

    def getInterfacesByBreif(self):
        result = self.Send(["terminal length 0", "show power inline"])
        values = result.splitlines()
        for(value in values):
            if(value.lower.startsWith('gi', 'fa', 'te')):
                Interfaces.append(
                    Interface.FromPower(value[0], value[1], value[2], value[3]))

    # Sender

    def Send(self, messages):
        for x in range(len(messages)):
            for n in range(0, 5):
                self.client.send("\n")
            self.client.send(messages[x])
            self.client.send("\n")

        time.sleep(2)
        return self.client.recv(50000)
