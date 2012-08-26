'''
Created on Aug 22, 2012

@author: xbx
'''
from plugin.base.main import BasePlugin


class Notes(BasePlugin):

    def task_default(self):
        print "nice plugin!"

    def task_add(self):
        self._input("enter note: ")

plugin_instance = Notes()
