import os
import sys
import re

def ip_detect(file):
    with open(file,'r') as f:
        for line in f:
            if(re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):[0-9]{1,5}$",line) != None):
                port=re.findall(r"\d{1,4}$",line)
                line = line.replace('\n',"")
                if(int(port[0]) < 2401):
                    print(line + " - " + "Valid (root priveleges required)")
                elif(int(port[0]) < 32768):
                    print(line + " - " + "Valid")
            else:
                line = line.replace('\n',"")
                print(line + " - " + "Invalid IP Address")


ip_detect("addys.in")

