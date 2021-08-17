from emitter import Emitter

# initialize emitter
e = Emitter("/storage/emulated/0/Download/out.py")
s = {}

def Compile(path):
    print("PlanetScript Compiler")
    with open(path, "r") as f:
        e.HeaderLine(f"def main():\n")
        for l in f:
            if "=" in l:
                # A variable declaration is the same in both PlanetScript and Python.
                # No changes needed, so we can simply add the line to the file.
                e.Line(f"    {l}\n")
                n = l[:l.find("=")-1]
                v = l[l.find("=")+3:-2]
                s[n] = v

            if "Print" in l:
                a = l[l.find("t")+3:-1]
                if "$" not in l:
                    if "    " not in l:
                        e.Line(f"    print(f\"{a}, end='')\n")
                    else:
                        e.Line(f"        print(f\"{a}, end='')\n")
                else:
                	if "    " not in l:
                		e.Line(f"    print({n}, end='')\n")
                	else:
                		e.Line(f"        print({n}, end='')\n")

            if "Input" in l:
                a = l[l.find("t")+2:]
                if "    " not in l:
                    e.Line(f"    {a.rstrip()} = input(\"\")\n")
                else:
                    e.Line(f"        {a} = input(\"\")\n")

            if "If" in l:
                c = l[3:l.find(":")]
                e.Line(f"    if {c}:\n")

            if "For" in l:
                c = l[4:l.find(":")]
                e.Line(f"    for {c}:\n")

            if "While" in l:
                c = l[6:l.find(":")]
                e.Line(f"    while {c}:\n")
            if l == "\n":
            	e.Line("\n")
            if "#" in l:
            	e.Line(f"    {l}")
    
    e.Line("    return 0\n")
    e.Line("\nmain()")
    print("Compiling finished...")
