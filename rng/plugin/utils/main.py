'''
Created on Aug 22, 2012

@author: xbx
'''
from plugin.base.main import BasePlugin
import calendar


class Utils(BasePlugin):

    def task_default(self):
        print "nice plugin!"

    def task_cal(self, parameters=None):
        print calendar.TextCalendar(calendar.SUNDAY)\
            .formatyear(2012, 1, 1, 3, 3)

    def task_help(self, parameters=None):
        for task in self._get_tasks():
            print task.replace("task_", "")

plugin_instance = Utils()
