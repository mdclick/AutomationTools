import paramiko
import time
from cisco.interface import Interface
from cisco.interface import InterfaceStatus
from cisco.interface import InterfaceProtocol


class Router:

    def __init__(self, client):
        self.client = client
        self.Interfaces = []

    # def GetInterfacesByPower(self):
    #     result = self.Send(["terminal length 0", "show power inline"])
    #     self.MapInterfacesByPower(result)

    # def MapInterfacesByPower(self, output):
    #     values = output.splitlines()
    #     for value in values:
    #         if value and value.lower().startswith(('gi', 'fa', 'te')):
    #             self.Interfaces.append(
    #                 Interface.FromPower(value[0], value[1], value[2]))

    def GetInterfacesByBreif(self):
        result = self.Send(["terminal length 0", "show power inline"])
        self.MapInterfacesByBreif(result)

    def MapInterfacesByBreif(self, output):
        values = output.splitlines()
        for value in values:
            if value and value.lower().startswith(('gi', 'fa', 'te')):
                items = filter(None, value.split(' '))
                status = InterfaceStatus.GetStatus(items[4])
                protocol = InterfaceProtocol.GetProtocol(items[-1])
                self.Interfaces.append(Interface.FromProtocol(
                    items[0], items[1], status, protocol))

    # Sender
    def Send(self, messages):
        for x in range(len(messages)):
            for n in range(0, 5):
                self.client.send("\n")
            self.client.send(messages[x])
            self.client.send("\n")

        time.sleep(2)
        return self.client.recv(50000)
