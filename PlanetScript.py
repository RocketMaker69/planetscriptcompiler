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
Keywords          = [
    "Let"
]

def GetKeyword(k):
    return k in Keywords



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

    def MakeTokens(self):
        if self.c in "+-*/":
            self.tok.append([To])
        if self.c in Letters:
            self.s = self.p
            while self.c in Letters:
                self.Advance()
            txt = self.i[self.s : self.p + 1]
            if GetKeyword(txt):
                self.tok.append(T
            



