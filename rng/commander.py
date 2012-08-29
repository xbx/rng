__author__ = "xbx"
__date__ = "$Aug 16, 2012 3:54:11 PM$"

from analyzer.RngLexicAnalyzer import RngLexicAnalyzer
from analyzer.RngLexicAnalyzer import RngInvalidCommandException
import os
import cmd2 as cmd
import importlib
import pkgutil
import logging


class RngCommander(cmd.Cmd):
    """ Route command to proper module/plugin """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.analyzer = RngLexicAnalyzer()
        self.current_plugin = None
        self.prompt = "> "

    def complete_in(self, text, line, start_index, end_index):
        plugins = [name for _, name, _ in pkgutil.iter_modules(['rng/plugin'])]
        if text:
            return [
                plugin for plugin in plugins
                if plugin.startswith(text)
            ]
        else:
            return plugins

    def precmd(self, line):
        return line

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def default(self, line):
        """Called on an input line when the command prefix
            is not recognized.
        """
        if self.current_plugin is None:
            return self._invalid_command()
        lexic = self._parse_line(line, 'in %s' % self.current_plugin)
        self._perform(lexic)

    """
        Commands methods. A command "foo" is routed to do_foo()
    """
    def do_help(self, line):
        if self.current_plugin is None:
            cmd.Cmd.do_help(self, line)
        else:
            self.default('help')

    def do_use(self, line):
        """ Select a plugin as default """
        lexic = self._parse_line(line, 'use')
        self._set_current_plugin(lexic.plugin)

    def do_shell(self, line):
        """ Execute command in terminal """
        os.system(line)

    def do_in(self, line):
        """ Nice command """
        lexic = self._parse_line(line, 'in')
        self._perform(lexic)

    def _parse_line(self, line, command=None):
        """ Returns the line parsed with lexical analysis """
        if command is not None:
            line = "%s %s" % (command, line)
        try:
            lexic = self.analyzer.analyze(line)
        except RngInvalidCommandException as e:
            raise e

        return lexic

    def _perform(self, lexic):
        """ Import needed module and executes the task """
        try:
            module_name = "plugin.%s.main" % (lexic.plugin)
            module = importlib.import_module(module_name)
        except Exception as e:
            logging.error("Unable to perform command: %s", e.message)
            raise Exception()
        if module.plugin_instance.task(lexic.action, lexic.parameters):
            self._invalid_command()

    def _invalid_command(self, line=None):
        print "Invalid command"
        return False

    def _set_current_plugin(self, plugin):
        self.current_plugin = plugin
        if(not plugin):
            self.prompt = "> "
        else:
            self.prompt = "(%s)> " % self.current_plugin
