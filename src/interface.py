
class InterfaceStatus:
    Up = 1
    Down = 0
    AdminstrativlyDown = -1


class InterfaceAdmin:
    Auto = 0
    Static = 1


class Interface:
    Name = ""
    Admin = InterfaceAdmin.Auto
    Operation = False
    Power = 0.0
    IP = ""
    Status = InterfaceStatus.Down
    Protocol = False

    @classmethod
    def FromPower(self, interface, admin, oper, power):
        self.Interface = interface
        self.Admin = admin
        self.Operation = oper
        self.Power = power

    @classmethod
    def FromProtocol(self, name, ip, protocol, status):
        self.Name = name
        self.IP = ip
        self.Protocol = protocol
        self.Status = status
