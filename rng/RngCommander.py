__author__ = "xbx"
__date__ = "$Aug 16, 2012 3:54:11 PM$"

from analyzer.RngLexicAnalyzer import RngLexicAnalyzer
from analyzer.RngLexicAnalyzer import RngInvalidCommandException
import os
import sys
import cmd2 as cmd
import importlib
import pkgutil


class RngCommander(cmd.Cmd):
    """ Route command to proper module/plugin """
    current_plugin = None
    analyzer = RngLexicAnalyzer()
    prompt = "> "

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.analizer = RngLexicAnalyzer()

    def complete_in(self, text, line, start_index, end_index):
        plugins = [name for _, name, _ in pkgutil.iter_modules(['plugin'])]
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

    def do_exit(self, line):
        """ Exits current plugin otherwise exits application """
        if self.current_plugin is not None:
            self.current_plugin = None
            self.prompt = "> "
        else:
            sys.exit(0)

    def do_use(self, line):
        """ Select a plugin as default """
        lexic = self._parse_line(line, 'use')
        self.current_plugin = lexic.plugin
        self.prompt = "(%s)> " % self.current_plugin

    def do_shell(self, line):
        """ Execute command in terminal """
        os.system(line)

    def do_in(self, line):
        """ Nice command """
        lexic = self._parse_line(line, 'in')
        self._perform(lexic)

    def _perform(self, lexic):
        """ Import needed module and executes the task """
        try:
            module_name = "plugin.%s.main" % (lexic.plugin)
            module = importlib.import_module(module_name)
        except:
            raise Exception()
        if module.plugin_instance.task(lexic.action):
            self._invalid_command()

    def _parse_line(self, line, command=None):
        """ Returns the line parsed with lexical analysis """
        if command is not None:
            line = "%s %s" % (command, line)
        try:
            lexic = self.analyzer.analyze(line)
        except RngInvalidCommandException as e:
            raise e

        return lexic

    def _invalid_command(self, line=None):
        print "Invalid command"
        return False
