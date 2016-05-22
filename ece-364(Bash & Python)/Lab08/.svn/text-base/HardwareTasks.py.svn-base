import os
import sys
import math
import re

def idIsAcceptable(ver_id):
    res = re.search(r"[^a-zA-Z0-9_]+",ver_id)
    if(res == None):
        return True
    return False


def processSingle(ver_assignment):
    res = re.search(r"\.(\w+)\((\w+)\)\s*$",ver_assignment)
    if res != None:
        valid1 = idIsAcceptable(res.group(1))
        valid2 = idIsAcceptable(res.group(2))

        if(valid1 == False or valid2 == False):
            raise ValueError(ver_assignment)
        else:
            return (res.group(1),res.group(2))
    else:
        raise ValueError(ver_assignment)


def processLine(ver_line):
    res = re.search(r"\s*(\w+)\s+(\w+)\s*\(([\s*\.\w+\(\w+\),?\s*]+)\)",ver_line)
    if(res != None):
        component = res.group(1)
        instance = res.group(2)
        assign_list=res.group(3).split(',')

        valid1 = idIsAcceptable(component)
        valid2 = idIsAcceptable(instance)
        final_alist = []

        if(valid1 == False):
            raise ValueError(ver_line)
        elif(valid2 == False):
            raise ValueError(ver_line)
        else:
            for assignment in assign_list:
                final_alist.append(processSingle(assignment))
        return (component,instance,tuple(final_alist))
    else:
        raise ValueError(ver_line)


