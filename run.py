import sys
from config import OPCODES
import code_generator
import re

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("USAGE python3 ./run.py [teal path] [output path] [Beautifier=1 or 0 (Optional, Default=1)]")
        sys.exit(0)
    
    error = None
    tealfile = open(sys.argv[1], "r")
    output = open(sys.argv[2], "w")

    beautifier = True
    if len(sys.argv) == 4:
        beautifier = int(sys.argv[3]) == 1
        
    _code_gen = code_generator.CODE_GENERATOR(beautifier=beautifier)

    for i, line in enumerate(tealfile):
        line = line.strip()
        if line.startswith("#pragma"):
            _code_gen.set_version(line+"\n")
            continue

        if line.find("//") != -1:
            line = line[:line.rindex("//")].strip()

        if len(line) == 0:
            continue
    
        #branch
        if line[-1] == ":":
            if _code_gen.beautifier:
                line += " // it is possible for stack to be confused"
            _code_gen.add_code(f"// {sys.argv[1]}:{i+1}")
            _code_gen.set_branch(line)
            continue

        if re.compile("[\w]{1,100}_[0-9]{1,3}").match(line):
            op = line[:line.rindex("_")]
            arg = line[line.rindex("_")+1:]
        else:
            op = line.split(" ")[0]
            arg = line[len(op)+1:]

        try: 
            OPCODES[op](_code_gen, arg)
        except Exception as e:
            error = (line, e)
            break

    
    #print("\n\n==============================\n")
#    print(_code_gen.get_result())

    if error:
        print("\n\nerror\n\n", error)
    else:
        output.write(_code_gen.get_result())
        
