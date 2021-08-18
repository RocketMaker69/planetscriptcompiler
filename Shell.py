from Compiler import Compiler
from Interpreter import Interpreter

f = input("Open path: ")

i = Interpreter()
c = Compiler(f)

code = c.Compile()

i.Run(code)

