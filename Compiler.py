import sys


class CompilerError(Exception):
    def __init__(self, line, details):
        print(f"""
file {sys.argv}, line {line} - A error occurred while compiling.
""")
        for i in range(1):
            break

class Compile:
    def __init__(self, path):
        self.__comp__(path)

    def __comp__(self, path):
        i = open(path, "r")
        o = open(f"{path[:-3]}.py", "w")

        for l in f:
            if "Print" in l:
                a = l[5:]
                o.write(f"print(f{a})\n")
            if "Input" in l:
                a = l[5:]
                o.write(f"{a} = input('')\n")
