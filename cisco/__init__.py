import sys
from cisco._version import __version__, __version_info__
from cisco.router import Router
from cisco.interface import (Interface,
                             InterfaceAdmin,
                             InterfaceProtocol,
                             InterfaceStatus)
__author__ = "Mohammad Mahmoud <abdalaal.mohamed@gmail.com>"
__license__ = "MIT License"
__all__ = [
    "Router",
    "Interface",
    "InterfaceAdmin",
    "InterfaceProtocol",
    "InterfaceStatus"
]
