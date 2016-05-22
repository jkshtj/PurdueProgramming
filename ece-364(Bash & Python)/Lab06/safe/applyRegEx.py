import sys
import os
import re

file= "SiteRegistration.txt"

def getRejectedUsers():
    user_list = []
    fin_list=[]
    with open(file,'r') as f:
        for line in f.readlines():
            #print(line)
            if(re.match(r"^[a-zA-Z, ]+[,; ]+$",line) != None):
                user_list.append(re.findall(r"^[a-zA-Z, a-zA-Z]+",line))
        #print(user_list)
        name_str=""
        for name in user_list:
            info = re.findall(r"([a-zA-Z ]+)",name[0])
            if(info[1] == " "):
                name_str += info[0]
                name_str = name_str.lstrip()
            else:
                name_str += info[1]
                name_str = name_str.strip()+" "+info[0]
                #print(name_str)
            fin_list.append(name_str)
            name_str=""
        fin_list.sort()
        print(fin_list)
    return fin_list


def getUsersWithEmails():
    dict = {}
    names = []
    with open(file,'r') as f:
        for line in f.readlines():
            if(re.match(r"^[a-zA-Z, ]+[a-zA-Z0-9-_\.@]+[,; ]+$",line) != None):
                info = re.match(r"^(?P<Names>[a-zA-Z, ]+)(?P<Email>[a-zA-Z0-9-_\.@])+[,; ]+$",line)
                names.append(info.group(0))
                print(names)


def getUsersWithoutEmails():
    user_list = []
    fin_list=[]
    with open(file,'r') as f:
        for line in f.readlines():
            #print( re.search("[a-zA-Z0-9_\.-]+@[a-zA-Z0-9_\.-]+[,; ]+",line))
            if(re.search("[a-zA-Z0-9_\.-]+@[a-zA-Z0-9_\.-]+[,; ]+",line) == None):
                if(re.search(r"[\w]+",line)):
                    user_list.append(re.findall(r"^[a-zA-Z, a-zA-Z]+",line))
        #print(user_list)
        name_str=""
        for name in user_list:
            info = re.findall(r"([a-zA-Z ]+)",name[0])
            if(info[1] == " "):
                name_str += info[0]
                name_str = name_str.lstrip()
            else:
                name_str += info[1]
                name_str = name_str.strip()+" "+info[0]
            fin_list.append(name_str)
            name_str=""
        fin_list.sort()
        print(fin_list)
    return fin_list

getUsersWithoutEmails()

def getUsersWithoutPhones():
    user_list = []
    fin_list=[]
    with open(file,'r') as f:
        for line in f.readlines():
            if(re.search(r"[0-9-\(\)]+",line) == None):
                if(re.search("[0-9]+",line) != None):
                    user_list.append(re.findall(r"^[a-zA-Z, a-zA-Z]+",line))
#        print(user_list)
        name_str=""
        for name in user_list:
            info = re.findall(r"([a-zA-Z ]+)",name[0])
            if(info[1] == " "):
                name_str += info[0]
                name_str = name_str.lstrip()
            else:
                name_str += info[1]
                name_str = name_str.strip()+" "+info[0]
            fin_list.append(name_str)
            name_str=""
        fin_list.sort()
        print(fin_list)
    return fin_list