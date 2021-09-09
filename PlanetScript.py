#####################################
# Imports
#####################################

from string import ascii_letters as Letters



#####################################
# Tokens
#####################################

TokenType_Number  = "Number"
TokenType_Symbol  = "Symbol"
TokenType_Keyword = "Keyword"

class Token:
    def __init__(self, k, t):
        self.k   = k
        self.t   = t
        self.tok = [self.k, self.t]



#####################################
# Lexer
#####################################

class Lexer:
    def __init__(self, i):
        self.i   = i
        self.p   = -1
        self.c   = ""
        self.tok = []
        self.Advance()

    def Advance(self):
        self.p += 1
        self.c = "\0" if self.p >= len(self.i) else self.i[self.p]

    def Peek(self):
        return "\0" if self.p + 1 >= len(self.i) else self.i[self.p + 1]

    def MakeTokens(self): pass

