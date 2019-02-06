import time
import cisco
import re


class Router:

    def __init__(self, client):
        self.client = client
        self.Interfaces = []

    def GetInterfacesByPower(self):
        result = self.Send(["terminal length 0", "show power inline"])
        self.MapInterfacesByPower(result)

    def MapInterfacesByPower(self, output):
        values = output.splitlines()
        for value in values:
            if value and value.lower().startswith(('gi', 'fa', 'te', 'tw')):
                items = filter(None, value.split(' '))
                admin = cisco.InterfaceAdmin.Get(items[1])
                oper = cisco.InterfaceOperation.Get(items[2])
                self.Interfaces.append(cisco.Interface.FromPower(
                    items[0], admin, oper, items[3]))

    def GetInterfacesByBrief(self):
        result = self.Send(["terminal length 0", "show ip int br"])
        self.MapInterfacesByBrief(result)

    def MapInterfacesByBrief(self, output):
        values = output.splitlines()
        for value in values:
            if value and value.lower().startswith(('gi', 'fa', 'te', 'tw')):
                items = filter(None, value.split(' '))
                status = cisco.InterfaceStatus.Get(items[4])
                protocol = cisco.InterfaceProtocol.Get(items[-1])
                self.Interfaces.append(cisco.Interface.FromProtocol(
                    items[0], items[1], status, protocol))

    def GetInterfacesByNeighbor(self):
        result = self.Send(
            ["terminal length 0", "show cdp neighbor detail | include (---|Platform|Interface)"])
        self.MapInterfacesByNeighbor(result)

    def MapInterfacesByNeighbor(self, output):
        values = output.splitlines()
        platform = None
        interface = None
        for value in values:
            if value and value.lower().startswith('platform'):
                items = filter(None, re.split(",|:", value))
                platform = items[1].strip()
            if value and value.lower().startswith('interface'):
                items = filter(None, re.split(",|:", value))
                interface = items[1].strip()
                if platform != None and interface != None:
                    self.Interfaces.append(
                        cisco.Interface.FromNeighbor(interface, platform))
                    platform = None
                    interface = None

    # Sender

    def Send(self, messages):
        for x in range(len(messages)):
            for n in range(0, 5):
                self.client.send("\n")
            self.client.send(messages[x])
            self.client.send("\n")

        time.sleep(2)
        return self.client.recv(50000)
