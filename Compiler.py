import sys

def CountTabs(l):
    s = 0
    e = 3
    c = 0
    while l[s:e] == "    ":
        s += 3
        e += 4
        c += 1
    return c

i       = open(sys.argv[1], "r")
o       = open("out.py", "r")
cim     = 0
methods = []

for l in i:
    if "Method" in l:
        mn = l[6:l.find("(")]
        ma = l[l.find("("):l.find(")")]
        o.write(f"def {mn}({ma}):\n")
        cim = 1
        methods.append(mn)
    if "Print" in l:
        a = l[5:-1]
        if cim == 0:
            for i in range(CountTabs(l)):
                o.write("    ")
        else:
            for i in range(CountTabs(l) + 1):
                o.write("    ")
        o.write(f"print(f{a})\n")
    if "Input" in l:
        a = l[5:-1]
        if cim == 0:
            for i in range(CountTabs(l)):
                o.write("    ")
        else:
            for i in range(CountTabs(l) + 1):
                o.write("    ")
        o.write(f"{a} = input(\"\")\n")
    if "}" in l:
        cim = 0
        for method in methods:
            if method in l:
                a = l[l.find(":")+1:]
                o.write(f"{method}({a})\n")
    if "#" in l:
        o.write(l)
