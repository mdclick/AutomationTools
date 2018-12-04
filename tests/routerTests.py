import os
import pytest
import cisco


def test_GetByStatus():
    assert('foo'.upper() == 'FOO')


def test_GivenShowBrief_RouterCouldCreateInterfaces():
    rt = cisco.Router(None)
    file = open(os.path.join(os.path.dirname(__file__), 'output.txt'), "r")
    rt.MapInterfacesByBreif(file.read())
    for interface in rt.Interfaces:
        print interface.Status
    assert len(rt.Interfaces) == 18
    assert rt.Interfaces[0].Name == 'FastEthernet0/0'
    assert rt.Interfaces[0].IP == 'unassigned'
    assert rt.Interfaces[0].Status == cisco.InterfaceStatus.AdminstrativlyDown
    assert rt.Interfaces[0].Protocol == cisco.InterfaceProtocol.Down
