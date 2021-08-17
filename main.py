from emitter import Emitter
import sys

# initialize emitter
e = Emitter()

e.Line("#include <stdio.h>;")
e.Line("")
e.Line("int main(void) {")

with open(sys.argv[1], "r") as f:
    for l in f:
        if "=" in l:
            n = l[:l.find("=")]
            v = l[l.find("=")+3:-1]
            e.Line(f"    float {n};\n")
            e.Line(f"    {n} = {v};\n")
        if "Print" in l:
            a = l[6:-1]
            e.Line(f"    printf({a});\n")
        if "Input" in l:
            a = l[6:-1]
            e.Line(f"    scanf(\"%f\", &{a});\n")
    e.Line(f"    return 0;\n")
    e.Line(f"}")
