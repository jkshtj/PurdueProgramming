import os
import sys
import math
import re
from HardwareTasks import*

def verilog2vhdl(ver_line):
    try:
        (component,instance,list) = processLine(ver_line)
    except ValueError:
        return "Error: Bad Line."

    final_list=[]
    for first,second in list:
        str = ""
        str += first + "=>" + second
        final_list.append(str)

    final_list = tuple(final_list)
    list_str = ", ".join(final_list)
    final_str = ""
    final_str += instance + ": " + component + " PORT MAP(" + list_str+");"
    return final_str


def convertNetlist(sourceFile,targetFile):
    input = open(sourceFile,'r')
    output = open(targetFile,'w+')
    str=""
    all_lines = input.readlines()
    for line in all_lines[:len(all_lines)-1]:
        str += verilog2vhdl(line) + '\n'
    str += verilog2vhdl(all_lines[len(all_lines)-1]).rstrip('\n')
    output.write(str)
    input.close()
    output.close()