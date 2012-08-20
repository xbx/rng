__author__ = "xbx"
__date__ = "$Aug 16, 2012 3:54:11 PM$"

from analyzer.RngLexicAnalyzer import RngLexicAnalyzer
import cmd

plugins = [
    'plug1',
    'plug2',
    'plug3',
]

class RngCommander(cmd.Cmd):
    """ Interactive console
        TODO docstrings
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.analizer = RngLexicAnalyzer()
    
    def complete_in(self, text, line, start_index, end_index):
        if text:
            return [
                plugin for plugin in plugins
                if plugin.startswith(text)
            ]
        else:
            return plugins
    
    def do_in(self, line):
        print line

