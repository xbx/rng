"""
Created on Aug 23, 2012

@author: xbx
"""
from db.handler import RngDbHandler


class BasePlugin(object):
    """
    This is the base plugin class that is extended by particular plugins
    """

    ERROR_INVALID_ACTION = 1
    SUCCESS_ACTION = 1

    def __init__(self):
        """
        Constructor
        """
        self.db = RngDbHandler(self.__class__.__name__)

    def task(self, action, parameters=None):
        """ Routes the task (action) to the proper method

        """
        if not action:
            return self.task_default()

        try:
            task_method = getattr(self, "task_" + action)
        except AttributeError:
            return self.ERROR_INVALID_ACTION

        return task_method(parameters)

    def task_default(self):
        """ To be performed on empty actions

         If this method is not overridden, it does nothing.

        """
        return self.SUCCESS_ACTION

    def task_help(self, parameters):
        """ To be performed on empty actions

         If this method is not overridden, it does nothing.

        """
        print "No help"

    def _input(self, prompt=""):
        return raw_input(prompt)

    def _get_tasks(self):
        return [task for task in dir(self) if task.startswith('task_')]
