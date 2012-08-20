#! /usr/bin/python

__author__="xbx"
__date__ ="$Aug 16, 2012 1:27:45 PM$"

import code
import sys
from RngCommander import *
import readline

class RngInteractiveTool():
    """ Interact with the user prompting for commands. """

    def __init__(self):
        commander = RngCommander()
        commander.cmdloop()

if __name__ == "__main__":
    RngInteractiveTool()
