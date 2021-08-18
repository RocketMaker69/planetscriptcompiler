class Interpreter:
    def __init__(self):
        self.s = []
        self.e = {}

    def Load(self, o):
        self.s.append(o)

    def SV(self, vn):
        vv = self.s.pop()
        self.e[vn] = vv

    def LV(vn):
        vv = self.e[vn]
        return vv

    def Run(self, code):
        Instructions = code["instructions"]
        Data = code["data"]
        for step in Instructions:
            i, a = step
            if i == "LOAD":
                self.Load(Data[a])
            elif i == "STORE VAR":
                self.SV(Data[a])
            elif i == "LOAD VAR":
                self.LV(Data[a])
            elif i == "PRINT":
                print(Data[a])
            elif i == "INPUT":
                x = input("")
                self.Load(x)
                self.SV("__input__")
