#                           CalcType Version 0.1 Alpha
#                    (For commands, refer to classesandshit.py)

import classes
import string
import sys
import math

# options
scriptPath = "script.ct"
labelMarker = "!"

file = open(scriptPath)
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

programdata = {
    "Loplist": [],
    "Registers": {},
    "LineData": {
        "ProgramLength": len(lines),
        "LineNumber": 0,
        "NextLine": 0
    },
    "LabelList": {}
}

for i in range(len(lines)):
    if "//" in lines[i]:
        lines[i] = lines[i].split("//", 1)[0]
    if labelMarker in lines[i]:
        programdata["LabelList"]["".join(lines[i][lines[i].index(labelMarker) + 1:]).strip()] = i
        lines[i] = lines[i].split(labelMarker, 1)[0]
        # print(lines[i])
# print(programdata["LabelList"])

while True:
    programdata["LineData"]["LineNumber"] = programdata["LineData"]["NextLine"]
    i = programdata["LineData"]["LineNumber"]

    if i >= programdata["LineData"]["ProgramLength"]:
        break

    programdata["LineData"]["NextLine"] += 1

    if lines[i] == "" or lines[i].isspace():
        continue

    TargetLine = lines[i].strip()
    # print("\n", TargetLine)
    Parts = TargetLine.split(" ")
    if len(Parts) == 1:
        continue
    Command = str(Parts[0])
    Args = (Parts[1:])

    if "" in Args:
        while "" in Args:
            Args.remove("")
    
    for i in range(len(Args)): # merge strings in Args
        # print(Args)
        
        # cpt x "test string thing" y
        if Args[i].startswith("\""):
            if Args[i].endswith("\""):
                continue
            TargetList = Args[i:]
            CompleteString = ""
            Offset = i

            for y in range(len(TargetList)):
                Args.pop(Offset)
                CompleteString += (" " + TargetList[y])
                # print(Args, CompleteString)
                if TargetList[y].endswith("\""):
                    Args.insert(Offset, CompleteString)
                    break

                if y == len(TargetList) - 1:
                    print(f"\033[1;31mLine {programdata['LineNumber'] + 1}: {TargetLine}\nSyntaxError: You didn't close your FUCKING string (ong)\033[0m")
                    sys.exit(1)

            Args[i] = CompleteString
            # print(Args)
            break
    
    for i in range(len(Args)): # replace vars for special case rsr
        if len(Args[i]) == 1 and Args[i][0].islower() and Command == "rsr":
            Args[i] = f"\"{Args[i]}\""

    if Command.startswith("//"):
        continue
    # print("stage 1: ", Args)

    if len(Args) == 0:
        continue

    for i in range(len(Args)):
        # print(Args[i])
        if Args[i][0].islower():
            if Args[i] == "lop":
                Args[i] = programdata["Loplist"][0]
            elif len(Args[i]) == 1:
                Args[i] = f'"{programdata["Registers"][Args[i]]}"'

    # print("stage 2: ", Args, programdata["LineData"]["LineNumber"] + 1)
    for i in range(len(Args)):
        # print(Args[i], programdata["Loplist"])
        Args[i] = eval(str(Args[i]))
    
    # print("stage 2: ", Args)
    
    # print(Command, Args)

    TargetClass = eval("classes.commands." + Command[0])
    empty = {}
    eval(f"TargetClass.{Command[1:]}(programdata, {Args})")
