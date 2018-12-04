
class InterfaceStatus:
    Up = "up"
    Down = "down"
    AdminstrativlyDown = "admin down"

    @classmethod
    def Get(self, value):
        if value.lower() == 'up':
            return self.Up
        if value.lower() == 'down':
            return self.Down
        if value.lower() == 'administratively':
            return self.AdminstrativlyDown


class InterfaceAdmin:
    Auto = "auto"
    Static = "static"

    @classmethod
    def Get(self, value):
        if value.lower() == 'auto':
            return self.Auto
        if value.lower() == 'static':
            return self.Static


class InterfaceProtocol:
    Down = "down"
    Up = "up"

    @classmethod
    def Get(self, value):
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
    def FromPower(cls, name, admin, oper, power):
        return cls(name, admin, oper, power, '', InterfaceStatus.Down, False)

    @classmethod
    def FromProtocol(cls, name, ip, status, protocol):
        return cls(name, '', False, 0.0, ip, status, protocol)
