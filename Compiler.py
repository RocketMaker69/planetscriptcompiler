import sys

i = open(sys.argv[1], "r")
o = open("out.c", "w")
M = []

for l in i:
    if "Method" in l:
        n = l[6:l.find(":")]
        a = l[l.find("("):l.find(")")]
        o.write(f"int {n}({a}) {\n")
        M.append(n)
    if "}" in l:
        o.write("}\n")
    if "#" in l:
        c = l[1:]
        o.write(f"//{c}\n")
    if "Print" in l:
        a = l[5:]
        o.write(f"printf({a});\n")
    if "Input" in l:
        a = l[5:]
        o.write(f"scanf("%f", &{a});\n")
    if "Variable" in l:
        a = l[8:]
        o.write(f"float {a};\n")
    for m in M:
        if m in l and "(" in l and ")" in l:
            a = l[l.find(":"):]
            o.write(f"{m}({a});\n")
