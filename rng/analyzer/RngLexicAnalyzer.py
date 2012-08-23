# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "xbx"
__date__ = "$Aug 16, 2012 4:41:48 PM$"

import re

class RngInvalidCommandException(Exception):
    pass

class RngLexic(object):
    plugin = None
    action = None

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

class RngLexicAnalyzer(object):

    def __init__(self):
        pass

    def analyze(self, text):
        lexic = re.match(r"(?P<command>\w+) (?P<plugin>\w+)( (?P<action>.+))?", text)
        if lexic == None:
            raise RngInvalidCommandException

        return RngLexic(lexic.groupdict())
    


