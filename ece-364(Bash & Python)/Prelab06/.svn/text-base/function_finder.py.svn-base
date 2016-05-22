import os
import sys
import re

def function_finder(file):
    if(os.path.exists(file)):
        if(not os.access(file,os.R_OK)):
            print("File is not readable")
            sys.exit()
    else:
        print("File doesn't exist")
        sys.exit()

    with open(file,'r') as f:
        for line in f:
            arg_num = 1
            a= re.match(r"^def", line)
            if a:
                line = re.findall("[a-zA-Z0-9=_-]+",line)
                print(line[1])
                for i in range(2,len(line)):
                    print("Arg" + str(arg_num) + ": "+line[i])
                    arg_num += 1


function_finder(sys.argv[1])