import os
import pytest
import cisco


def test_GivenShowBrief_RouterCouldCreateInterfaces():
    rt = cisco.Router(None)
    file = open(os.path.join(os.path.dirname(
        __file__), 'outputBrief.txt'), "r")
    rt.MapInterfacesByBrief(file.read())
    assert len(rt.Interfaces) == 18
    assert rt.Interfaces[0].Name == 'FastEthernet0/0'
    assert rt.Interfaces[0].IP == None
    assert rt.Interfaces[0].Status == cisco.InterfaceStatus.AdministrativelyDown
    assert rt.Interfaces[0].Protocol == cisco.InterfaceProtocol.Down


def test_GivenShowPower_RouterCouldCreateInterfaces():
    rt = cisco.Router(None)
    file = open(os.path.join(os.path.dirname(
        __file__), 'outputPower.txt'), "r")
    rt.MapInterfacesByPower(file.read())
    assert len(rt.Interfaces) == 72
    assert rt.Interfaces[0].Name == 'Gi1/0/1'
    assert rt.Interfaces[0].Admin == cisco.InterfaceAdmin.Static
    assert rt.Interfaces[0].Operation == cisco.InterfaceOperation.On
    assert rt.Interfaces[0].Power == 10.2


def test_GivenShowNeighbor_RouterCouldCreateInterfaces():
    rt = cisco.Router(None)
    file = open(os.path.join(os.path.dirname(
        __file__), 'outputNeighbor.txt'), "r")
    rt.MapInterfacesByNeighbor(file.read())
    assert len(rt.Interfaces) == 3
    assert rt.Interfaces[0].Name == 'FastEthernet0/24'
    assert rt.Interfaces[0].Neighbor == 'MikroTik'
    assert rt.Interfaces[1].Name == 'FastEthernet0/10'
    assert rt.Interfaces[1].Neighbor == 'Cisco IP Phone 7911'
