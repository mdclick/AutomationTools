import os
import pytest
import cisco


def test_GetByStatus():
    assert('foo'.upper() == 'FOO')


def test_GivenShowBrief_RouterCouldCreateInterfaces():
    rt = cisco.Router(None)
    file = open(os.path.join(os.path.dirname(
        __file__), 'outputBreif.txt'), "r")
    rt.MapInterfacesByBreif(file.read())
    assert len(rt.Interfaces) == 18
    assert rt.Interfaces[0].Name == 'FastEthernet0/0'
    assert rt.Interfaces[0].IP == 'unassigned'
    assert rt.Interfaces[0].Status == cisco.InterfaceStatus.AdminstrativlyDown
    assert rt.Interfaces[0].Protocol == cisco.InterfaceProtocol.Down


def test_GivenShowPower_RouterCouldCreateInterfaces():
    rt = cisco.Router(None)
    file = open(os.path.join(os.path.dirname(
        __file__), 'outputPower.txt'), "r")
    rt.MapInterfacesByPower(file.read())
    assert len(rt.Interfaces) == 72
    assert rt.Interfaces[0].Name == 'Gi1s/0/1'
    assert rt.Interfaces[0].Admin == cisco.InterfaceAdmin.Static
    assert rt.Interfaces[0].Operation == cisco.InterfaceOperation.On
    assert rt.Interfaces[0].Power == "10.20"
