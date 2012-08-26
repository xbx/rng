__author__ = "xbx"
__date__ = "$Aug 16, 2012 1:27:45 PM$"

from RngCommander import RngCommander


class RngInteractiveTool(object):
    """ Interact with the user prompting for commands. """

    def __init__(self):
        commander = RngCommander()
        commander.cmdloop("welcome")

if __name__ == "__main__":
    RngInteractiveTool()
