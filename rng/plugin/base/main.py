"""
Created on Aug 23, 2012

@author: xbx
"""


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

    def task(self, action):
        """ Routes the task (action) to the proper method

        """
        if not action:
            return self.task_default()

        try:
            task_method = getattr(self, "task_" + action)
        except AttributeError:
            return self.ERROR_INVALID_ACTION

        return task_method()

    def task_default(self):
        """ To be performed on empty actions

         If this method is not overridden, it does nothing.

        """
        return self.SUCCESS_ACTION

    def _input(self, prompt=""):
        return raw_input(prompt)
