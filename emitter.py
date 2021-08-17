class Emitter:
    def __init__(self):
        with open("out.py", "w") as f:
            self.f = f
    
    def Line(self, line):
        self.f.write(line)
