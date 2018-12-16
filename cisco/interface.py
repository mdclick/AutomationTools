
class InterfaceOperation:
    On = "on"
    Off = "off"

    @classmethod
    def Get(self, value):
        if value.lower() == 'on':
            return self.On
        if value.lower() == 'off':
            return self.Off


class InterfaceStatus:
    Up = "up"
    Down = "down"
    AdministrativelyDown = "admin down"

    @classmethod
    def Get(self, value):
        if value.lower() == 'up':
            return self.Up
        if value.lower() == 'down':
            return self.Down
        if value.lower() == 'administratively':
            return self.AdministrativelyDown


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
    Name = None
    Admin = InterfaceAdmin.Auto
    Operation = InterfaceOperation.Off
    Power = 0.0
    IP = None
    Status = InterfaceStatus.Down
    Protocol = InterfaceProtocol.Down
    Neighbor = None

    def __init__(self, name, admin, operation, power, ip, status, protocol, neighbor):
        self.Admin = admin
        self.Operation = operation
        self.Power = float(power)
        self.Name = name
        self.IP = ip
        self.Protocol = protocol
        self.Status = status
        self.Neighbor = neighbor

    @classmethod
    def FromPower(cls, name, admin, operation, power):
        return cls(name, admin, operation, power, None, InterfaceStatus.Down, InterfaceProtocol.Down, None)

    @classmethod
    def FromProtocol(cls, name, ip, status, protocol):
        return cls(name, None, InterfaceOperation.Off, 0.0, None, status, protocol, None)

    @classmethod
    def FromNeighbor(cls, name, neighbor):
        return cls(name, None, InterfaceOperation.Off, 0.0, None, InterfaceStatus.Down, InterfaceProtocol.Down, neighbor)
