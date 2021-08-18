def Compile(file):
    newCode = {
        "instructions": [],
        "data"        : []
    }
    f = open(file, "w")
    for l in f:
        if "Print" in l:
            arg = l[5:]
            newCode["data"].append(arg)
            newCode["instructions"].append(("PRINT", newCode["data"].index(arg)))
        if "Input" in l:
            arg = l[5:]
            newCode["data"].append(arg)
            newCode["instructions"].append(("INPUT", newCode["data"].index(arg)))
