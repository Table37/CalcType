# Classes and shit

import math
import sys

class CoreFunctions:
    def AddToLop(programdata: dict, value):
        programdata["Loplist"].insert(0, value)

class commands:
    class c:
        # Core
        def pt(programdata, args: list):
            # PrinT
            toprint = str(args[0])
            if len(args) > 1:
                for i in range(1, len(args)):
                    toprint += str(args[i])
            print(toprint)
        
        def ui(programdata: dict, args: list):
            # User Input
            ToPrint = input(args[0])
            ToPrint = f"\"{ToPrint}\""
            CoreFunctions.AddToLop(programdata, f"{ToPrint}")
        
        def gt(programdata: dict, args: list):
            # Go To
            if programdata["LineData"]["ProgramLength"] < args[0] or args[0] < 0:
                print(f"Error: Line {args[0]} does not exist.")
                sys.exit(1)
            else:
                programdata["LineData"]["NextLine"] = args[0] - 1
        
        def it(programdata: dict, args: list):
            # If True
            if eval(f"\"{args[0]}\" {args[1]} \"{args[2]}\""):
                pass
            else:
                programdata["LineData"]["NextLine"] += 1
        
        def gl(programdata: dict, args: list):
            # Go to Label
            programdata["LineData"]["NextLine"] = programdata["LabelList"][args[0]]
        
        def ws(programdata: dict, args: list):
            # Wait for Seconds
            import time
            time.sleep(float(args[0]))

    
    class t:
        # tests
        def dt(programdata, args: list):
            # do thing
            programdata["Loplist"].insert(0, args[0])
        
    class m:
        # math
        def ad(programdata: dict, args: list):
            # ADd
            programdata["Loplist"].insert(0, int(args[0]) + int(args[1]))
        
        def sb(programdata: dict, args: list):
            # SuBtract
            programdata["Loplist"].insert(0, int(args[0]) - int(args[1]))
        
        def ml(programdata: dict, args: list):
            # MuLtiply
            programdata["Loplist"].insert(0, int(args[0])*int(args[1]))
        
        def dv(programdata: dict, args: list):
            # DiVide
            programdata["Loplist"].insert(0, int(args[0])/int(args[1]))
        
        def ex(programdata: dict, args: list):
            # EXponent
            programdata["Loplist"].insert(0, int(args[0])**int(args[1]))
        
        def sr(programdata: dict, args: list):
            # Square Root
            programdata["Loplist"].insert(0, math.sqrt(int(args[0])))
    
    class r:
        # register
        def sr(programdata: dict, args: list):
            # Set Register
            programdata["Registers"][args[0]] = args[1]
    
    class s:
        # string
        def cs(programdata: dict, args: list):
            # Combine String
            CompleteString = ""
            for i in range(len(args)):
                CompleteString += str(args[i])
            CoreFunctions.AddToLop(programdata, f"\"{CompleteString}\"")
    
    class a:
        # array
        def ii(programdata: dict, args: list):
            # If In array
            if args[0] in args[1]:
                pass
            else:
                programdata["LineData"]["NextLine"] += 1
        
        def na(programdata: dict, args: list):
            # New Array
            NewArray = []
            for i in range(len(args)):
                NewArray.append(args[i])
            CoreFunctions.AddToLop(programdata, NewArray)