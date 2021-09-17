from string import ascii_letters as _l

class Parser:
    def __init__(self, text):
        self.t   = text
        self.i   = -1
        self.c   = ""
        self.ast = {} # AST is used because PlanetScript is interpreted.

    def advance(self):
        self.i += 1
        self.c = self.t[self.i] if self.i < len(self.t) else "\0"

    def peek(self):
        return self.t[self.i + 1] if self.i + 1 < len(self.t) else "\0"

    def make_ast(self):
        while self.c != "\0":
            if self.c in "0123456789":
                s = self.p
                while self.c in "0123456789.":
                    self.advance()
                self.ast["num"] = float(self.t[s : self.p + 1])
            elif self.c in _l:
                s = self.p
                while self.c in _l:
                    self.advance()
                st = self.t[s : self.p]
                if st not in self.vd:
                    self.ast[st] = {}
                else: 
                    self.ast["var"] = st
            elif self.c in " \t\r":
                self.advance()
 
