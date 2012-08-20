# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "xbx"
__date__ = "$Aug 16, 2012 4:41:48 PM$"

from plex import *


class RngLexicAnalyzer(object):

    space = Any(" \t\n")

    def some(self, text):
        return "some", text

    lexicon = Lexicon([
        (Str('in '), Begin('set_plugin_name')),
        (Str('on '), some),
        State('set_plugin_name', [
            (Rep1(Range("azAZ")), 'plugin'),
            (space, Begin(''))
        ]),
        State('set_plugin_action', [
            (Rep1(Range("azAZ")), 'plugin_action')
        ])
    ])

    def __init__(self):
        pass

    def analyze(self, stream):
        scanner = Scanner(self.lexicon, stream)
        try:
            result = scanner.read()
        except errors.UnrecognizedInput:
            return None
        return result


