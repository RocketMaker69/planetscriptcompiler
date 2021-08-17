from emitter import Emitter
import sys

# initialize emitter
e = Emitter()

with open(sys.argv[1], "r") as f:
    for l in f:
        if "=" in l:
            n = l[:l.find("=")]
            v = l[l.find("=")+3:-1]
            e.Line(f"{n} = {v};\n")
        if "Print" in l:
            a = l[6:-1]
            e.Line(f"print(f\"{a}\")\n")
        if "Input" in l:
            a = l[5:]
            e.Line(f"{a} = input(\"\")\n")
