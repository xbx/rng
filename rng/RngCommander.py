__author__ = "xbx"
__date__ = "$Aug 16, 2012 3:54:11 PM$"

from analyzer.RngLexicAnalyzer import RngLexicAnalyzer, RngInvalidCommandException
import cmd
import sys
import importlib

plugins = [
    'plug1',
    'plug2',
    'plug3',
]

class RngCommander(cmd.Cmd):
    """ Interactive console
        TODO docstrings
    """
    current_plugin = None
    analyzer = RngLexicAnalyzer()
    prompt = "> "

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
    
    def precmd(self, line):
        return line
    
    def do_exit(self, line):
        if self.current_plugin != None:
            self.current_plugin = None
            self.prompt = "> "
        else:
            sys.exit(0)
            
    def do_use(self, line):
        lexic = self._parse_line(line, 'use')
        self.current_plugin = lexic.plugin
        self.prompt = "(%s)> " % self.current_plugin
    
    def default(self, line):
        if self.current_plugin == None:
            return self._invalid_command()
        lexic = self._parse_line(line, 'in %s' % self.current_plugin)
        self._perform(lexic)
        
    def do_shell(self, line):
        """ Execute command in terminal """
        import os
        os.system(line)
    
    def do_in(self, line):
        """ Nice command """
        lexic = self._parse_line(line, 'in')
        self._perform(lexic)
        
    def _perform(self, lexic):
        
        try:
            module_name = "plugin.%s" % lexic.plugin
            module = importlib.import_module(module_name)
        except:
            raise Exception()
        
        module.plugin_instance.task(lexic.action)
        
    def _parse_line(self, line, command = None):
        if command != None:
            line = "%s %s" % (command, line)
        try:
            lexic = self.analyzer.analyze(line)
        except RngInvalidCommandException as e:
            raise e
        
        return lexic
        
    def _invalid_command(self, line = None):
        print "Invalid command"
        return False

