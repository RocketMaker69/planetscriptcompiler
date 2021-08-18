class Emitter:
    def __init__(self, outf):
        f = open(outf, "w")
        self.f = f
        self.HeaderLine("#include <stdio.h>;\n")
        self.HeaderLine("int main() {")

    def HeaderLine(self, l):
        self.Line(l)

    def Line(self, l):
        self.f.write(l + "\n")
