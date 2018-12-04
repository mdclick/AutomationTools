
class InterfaceStatus:
    Up = 1
    Down = 0
    AdminstrativlyDown = -1

    @classmethod
    def GetStatus(self, value):
        if value.lower() == 'up':
            return self.Up
        if value.lower() == 'down':
            return self.Down
        if value.lower() == 'administratively':
            return self.AdminstrativlyDown


class InterfaceAdmin:
    Auto = 0
    Static = 1


class InterfaceProtocol:
    Down = 0
    Up = 1

    @classmethod
    def GetProtocol(self, value):
        if value.lower() == 'up':
            return self.Up
        if value.lower() == 'down':
            return self.Down


class Interface:
    Name = ""
    Admin = InterfaceAdmin.Auto
    Operation = False
    Power = 0.0
    IP = ""
    Status = InterfaceStatus.Down
    Protocol = False

    def __init__(self, name, admin, operation, power, ip, status, protocol):
        self.Admin = admin
        self.Operation = operation
        self.Power = power
        self.Name = name
        self.IP = ip
        self.Protocol = protocol
        self.Status = status

    @classmethod
    def FromPower(cls, admin, oper, power):
        return cls('', admin, oper, power, '', InterfaceStatus.Down, False)

    @classmethod
    def FromProtocol(cls, name, ip, status, protocol):
        return cls(name, '', False, 0.0, ip, status, protocol)
