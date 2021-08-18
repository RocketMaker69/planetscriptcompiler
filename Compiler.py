class Compiler:
    def __init__(self, f):
        self.f = f

    def Compile():
        newCode = {"instructions": [],"data": []}
        f = open(self.f, "w")
        for l in f:
            if "Print" in l:
                arg = l[5:]
                newCode["data"].append(arg)
                newCode["instructions"].append(("PRINT", newCode["data"].index(arg)))
            if "Input" in l:
                arg = l[5:]
                newCode["data"].append(arg)
                newCode["instructions"].append(("INPUT", newCode["data"].index(arg)))
        
        return newCode
