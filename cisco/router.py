import paramiko
import time
import cisco


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
            if value and value.lower().startswith(('gi', 'fa', 'te')):
                items = filter(None, value.split(' '))
                admin = cisco.InterfaceAdmin.Get(items[1])
                oper = cisco.InterfaceOperation.Get(items[2])
                self.Interfaces.append(cisco.Interface.FromPower(
                    items[0], admin, oper, items[3]))

    def GetInterfacesByBreif(self):
        result = self.Send(["terminal length 0", "show ip int br"])
        self.MapInterfacesByBreif(result)

    def MapInterfacesByBreif(self, output):
        values = output.splitlines()
        for value in values:
            if value and value.lower().startswith(('gi', 'fa', 'te')):
                items = filter(None, value.split(' '))
                status = cisco.InterfaceStatus.Get(items[4])
                protocol = cisco.InterfaceProtocol.Get(items[-1])
                self.Interfaces.append(cisco.Interface.FromProtocol(
                    items[0], items[1], status, protocol))

    # client
    def Send(self, messages):
        for x in range(len(messages)):
            for n in range(0, 5):
                self.client.send("\n")
            self.client.send(messages[x])
            self.client.send("\n")

        time.sleep(2)
        return self.client.recv(50000)
