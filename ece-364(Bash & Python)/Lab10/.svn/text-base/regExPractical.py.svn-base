import os
import re
import sys

def getAddress(sentence):
    aph="ABCDEFabcdef"
    mac = re.search(r"[0-9A-Fa-f]+[:|-]{1}[0-9A-Fa-f]+[:|-]{1}[0-9A-Fa-f]+[:|-]{1}[0-9A-Fa-f]+[:|-]{1}[0-9A-Fa-f]+[:|-]{1}[0-9A-Fa-f]+",sentence)
    if mac != None:
        return mac.group(0)

def getSwitches(commandline):
    switches = re.findall(r"[\\|+]{1}([a-z]{1})\s*([\w/*:*\.*]+)",commandline)
    switches = sorted(switches)
    #print(switches)
    if switches != None:
       return switches

def getElements(fullAddress):
    url = re.findall(r"[http://|https://]{1}([\w+\.*]+)/([a-zA-Z0-9]+)/(\w+)",fullAddress)
    if len(url) == 0:
        return None
    res=[]
    for item in url[0]:
        if item != "":
            res.append(item)
        else:
            return None
    print(res)
    return tuple(res)

getElements("http://www.yahoo.com/AboutUs/Vision/Leadership")
