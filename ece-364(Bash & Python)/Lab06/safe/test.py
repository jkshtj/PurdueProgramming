import sys
import os
import re

file = "SiteRegistration.txt"
main_dict={} ## stores all the infor-->key is person's name
name=""

## making a dictionary with all the info for all the people in the file
with open(file,'r') as f:
    for line in f.readlines():
        line = line.replace('\n',"")
        info = re.search(r"^(\w+[,\s]*)(\w+)*[,;\s]*[a-z]([[\w\._]*@*[\w\.]*]*)[,;\s]*([\d*\-*\(?\)?\s*]*)[,;\s]*([\w\s*]*)$", line)
        #print(info.group(5))
        if(re.search(r",",info.group(1)) == None):
            name += info.group(1) + info.group(2)
        else:
            name += info.group(2) + " " + info.group(1).replace(',','')
        main_dict[name] = (info.group(3),info.group(4),info.group(5))
        name=""


def getRejectedUsers():


def getUsersWithCompleteInfo():


def getUsersWithEmails():


def getUsersWithPhones():


def getUsersWithStates():


def getUsersWithoutEmails():


def getUsersWithoutPhones():


def getUsersWithoutStates():
