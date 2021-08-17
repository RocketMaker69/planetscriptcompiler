class Emitter:
    def __init__(self, path):
        with open(path, "w") as f:
            self.f = f

    def HeaderLine(self, line):
        self.f.write(line)
    
    def Line(self, line):
        self.f.write(line)
