# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "xbx"
__date__ = "$Aug 16, 2012 4:41:48 PM$"

import reflex


class RngLexicAnalyzerReflex(object):

    def string_text(self, token_stream):
        print self.scanner.token.value

    def __init__(self):
        pass

    def analyze(self, stream):
        scanner = reflex.scanner("start")
        TOKEN_IDENT = 1
        TOKEN_NUMBER = 2
        scanner.rule("[a-zA-Z_][\w_]*", token=TOKEN_IDENT)
        scanner.rule("0x[\da-fA-F]+|\d+", token=TOKEN_NUMBER)
        TOKEN_STRING = 3
        scanner.rule("in", tostate="plugin")

        scanner.state("plugin")
        scanner.rule(" ", tostate="action")
        scanner.rule("[a-zA-Z]+", self.string_text)

        token_iter = scanner(stream)
        for token in token_iter:
            print(token)




