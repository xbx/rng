'''
Created on Aug 22, 2012

@author: xbx
'''
from plugin.base.main import BasePlugin
from datetime import datetime


class Notes(BasePlugin):

    def task_default(self):
        print "nice plugin!"

    def task_add(self, parameters=None):
        if parameters is not None:
            text = parameters
        else:
            text = self._input("enter note: ")
        note = {'text': text,
                'timestamp': datetime.now()}
        self.db.insert(note)

    def task_find(self, parameters=None):
        if parameters is None:
            notes = self.db.find()
        else:
            # TODO custom parameters
            notes = self.db.find(parameters)
        for note in notes:
            print "[%s]\n%s\n" % (note['timestamp'], note['text'])

plugin_instance = Notes()
