#import libs
from ast import literal_eval
import sys, time

#settings
ram = []
loop = False
sector = 0

#code
with open("code", "r", encoding="utf-8") as f:
    string = f.read()

#interpreter
def interpret(stringcode, repeat):
    global sector, ram
    loop = False
    arrram = ""
    for okak in range(repeat):
        for i in range(len(stringcode)):
            if loop == False:
                if stringcode[i] == "@":
                    loop = True
                if stringcode[i] == "i":
                    with open(ram[sector], "r") as f:
                        interpret(f.read(),1)
                elif stringcode[i] == "/":
                    ram.append(0)
                elif stringcode[i] == "%":
                    ram[sector] = 0
                elif stringcode[i] == "~":
                    time.sleep(ram[sector])
                elif stringcode[i] == "+":
                    ram[sector] += 1
                elif stringcode[i] == "-":
                    ram[sector] -= 1
                elif stringcode[i] == ".":
                    print(ram[sector])
                elif stringcode[i] == ",":
                    print(ram[sector], end='')
                elif stringcode[i] == ">":
                    sector += 1
                elif stringcode[i] == "<":
                    sector -= 1
                elif stringcode[i] == ":":
                    print(chr(ram[sector]))
                elif stringcode[i] == ";":
                    print(chr(ram[sector]), end='')
                elif stringcode[i] == "|":
                    print(" ", end='')
                elif stringcode[i] == "$":
                    arr = literal_eval(ram[sector])
                    interpret(arr[0], 1)
                    interpret(arr[1], arr[2])
                elif stringcode[i] == "#":
                    print(ram)
                elif stringcode[i] == "^":
                    ram = []
                    sector = 0
            else:
                if stringcode[i] != "@":
                    arrram += stringcode[i]
                if stringcode[i] == "@":
                    ram[sector] = arrram
                    arrram = ""
                    loop = False
                    print(arrram)

interpret(string, 1)
while True:
    time.sleep(1)
