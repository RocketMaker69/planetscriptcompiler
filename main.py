from emitter import Emitter
import sys

# initialize emitter
e = Emitter()

with open(sys.argv[1], "r") as f:
    for l in f:
        if "=" in l:
            # A variable declaration is the same in both PlanetScript and Python.
            # No changes needed, so we can simply add the line to the file.
            e.Line(l)
        if "Print" in l:
            a = l[l.find("t")+2:-1]
            if "\t" not in l:
                e.Line(f"print(f\"{a}\")\n")
            else:
                e.Line(f"    print(f\"{a}\")\n")
        if "Input" in l:
            a = l[l.find("t")+2:]
            if "\t" not in l:
                e.Line(f"{a} = input(\"\")\n")
            else:
                e.Line(f"    {a} = input(\"\")\n")
        if "If" in l:
            c = l[3:l.find(":")]
            e.Line(f"if {c}:\n")
