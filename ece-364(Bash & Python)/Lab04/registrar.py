import sys
import glob
import re
import os

def getDetails():
    file_list = []
    ledger = {} ## contains student names and their ids
    result = {}

    with open('files/students.txt','r') as f:
        f.readline()
        f.readline()
        for line in f:
            names = re.findall('[A-Za-z ]+', line)[0]
            names = names.rstrip()
            ids = re.findall('[0-9-]+',line)
            ledger[ids[0]] = names

    file_list = glob.glob('files/EECS*.txt')
    for file in file_list:
        with open(file,'r') as f:
            cid = re.split('_|\.', os.path.basename(file))[0]
            cid = re.findall('[0-9]+',cid)
            #print(cid)
            f.readline()
            f.readline()

            for line in f:
                ids,scores = re.split(' +',line)
                #print(ids)
                #print(scores)
                if ledger.get(ids) in result:
                    result[ledger.get(ids)].add((cid[0],int(scores)))
                else:
                    #result[ledger.get(ids)] = []
                    result[ledger.get(ids)] = {(cid[0],int(scores))}

    #print (result)
    return result


def getStudentList(classNumber):
    file_list = []
    names = []
    ledger = {}
    names_in_file = []
    if os.path.exists('files/EECS' + str(classNumber) +'.txt') == False:
        return names
    else:
        with open('files/students.txt','r') as f:
            f.readline()
            f.readline()
            for line in f:
                names = re.findall('[A-Za-z ]+', line)[0]
                names = names.rstrip()
                ids = re.findall('[0-9-]+',line)
                ledger[ids[0]] = names

        with open('files/EECS' + str(classNumber) +'.txt', 'r') as f:  ## opening the curr file
            f.readline()
            f.readline()
            for line in f:
                ids,scores = re.split(' +',line)
                names_in_file.append(ledger.get(ids))
            names_in_file.sort()
            print(names_in_file)

    return names_in_file


def searchForName(studentName):
    file_list = []
    names = []
    ledger = {}
    sid = 0
    result = {}
    flag = 0

    with open('files/students.txt','r') as f:
        f.readline()
        f.readline()
        for line in f:
            names = re.findall('[A-Za-z ]+', line)[0]
            names = names.rstrip()
            ids = re.findall('[0-9-]+',line)
            ledger[names] = ids[0]

        sid = ledger.get(studentName)  ## got id

        file_list = glob.glob('files/EECS*.txt')

        for file in file_list:
            with open(file,'r') as f:
                cid = re.split('_|\.', os.path.basename(file))[0]
                cid = re.findall('[0-9]+',cid)
                #print(cid)
                f.readline()
                f.readline()

                for line in f:
                    ids,scores = re.split(' +',line)
                    if sid == ids:
                        flag = 1
                        result[cid[0]] = int(scores)
        print (result)
    if flag == 0:
        return {}
    else:
        return result


def searchForID(studentID):
    file_list = []
    names = []
    ledger = {}
    sid = studentID
    result = {}
    flag = 0

    file_list = glob.glob('files/EECS*.txt')

    for file in file_list:
        with open(file,'r') as f:
            cid = re.split('_|\.', os.path.basename(file))[0]
            cid = re.findall('[0-9]+',cid)

            f.readline()
            f.readline()

            for line in f:
                ids,scores = re.split(' +',line)
                if sid == ids:
                    flag = 1
                    result[cid[0]] = int(scores)
    print (result)
    if flag == 0:
        return {}
    else:
        return result


def findScore(studentName,classNumber):
    grade = 0
    file_list = []
    names = []
    ledger = {}
    sid = 0
    result = {}
    flag = 0

    if os.path.exists('files/EECS' + classNumber +'.txt') == False:
        return None

    with open('files/students.txt','r') as f:
        f.readline()
        f.readline()
        for line in f:
            names = re.findall('[A-Za-z ]+', line)[0]
            names = names.rstrip()
            ids = re.findall('[0-9-]+',line)
            ledger[names] = ids[0]

        sid = ledger.get(studentName)  ## got id

        with open('files/EECS' + classNumber +'.txt','r') as f:
            f.readline()
            f.readline()

            for line in f:
                ids,scores = re.split(' +',line)
                if sid == ids:
                    flag = 1
                    grade = int(scores)
        print (grade)
    if flag == 0:
        return None
    else:
        return grade


def getHighest(classNumber):
    file_list = []
    result = ()
    flag = 0
    max_score = 0
    names = []
    ledger = {}
    result = {}
    flag = 0

    if os.path.exists('files/EECS' + classNumber +'.txt') == False:
        return ()

    with open('files/students.txt','r') as f:
        f.readline()
        f.readline()
        for line in f:
            names = re.findall('[A-Za-z ]+', line)[0]
            names = names.rstrip()
            ids = re.findall('[0-9-]+',line)
            ledger[ids[0]] = names

    if os.path.exists('files/EECS' + classNumber +'.txt') == False:
        return None


    with open('files/EECS' + classNumber +'.txt','r') as f:
        f.readline()
        f.readline()

        for line in f:
            ids,scores = re.split(' +',line)
            if int(scores) > max_score:
                flag = 1
                max_score = int(scores)
                result=(ledger.get(ids),int(scores))
    print (result)
    if flag == 0:
        return ()
    else:
        return result


def getLowest(classNumber):
    result = ()
    flag = 0
    min_score = 1000
    names = []
    ledger = {}
    flag = 0

    if os.path.exists('files/EECS' + classNumber +'.txt') == False:
        return ()

    with open('files/students.txt','r') as f:
        f.readline()
        f.readline()
        for line in f:
            names = re.findall('[A-Za-z ]+', line)[0]
            names = names.rstrip()
            ids = re.findall('[0-9-]+',line)
            ledger[ids[0]] = names

    if os.path.exists('files/EECS' + classNumber +'.txt') == False:
        return None


    with open('files/EECS' + classNumber +'.txt','r') as f:
        f.readline()
        f.readline()

        for line in f:
            ids,scores = re.split(' +',line)
            if int(scores) < min_score:
                flag = 1
                min_score = int(scores)
                result=(ledger.get(ids),int(scores))
    print (result)
    if flag == 0:
        return ()
    else:
        return result


def getAverageScore(studentName):
    file_list = []
    names = []
    ledger = {}
    avg = 0
    count = 0
    sum = 0
    sid = 0

    with open('files/students.txt','r') as f:
        f.readline()
        f.readline()
        for line in f:
            names = re.findall('[A-Za-z ]+', line)[0]
            names = names.rstrip()
            ids = re.findall('[0-9-]+',line)
            ledger[names] = ids[0]

    if studentName not in ledger:
        return None
    else:
       sid = ledger.get(studentName)

    file_list = glob.glob('files/EECS*.txt')

    for file in file_list:
        with open(file,'r') as f:
            f.readline()
            f.readline()

            for line in f:
                ids,scores = re.split(' +',line)
                if sid == ids:
                    count = count + 1
                    sum = sum + int(scores)

    avg = float(sum/count)
    print(avg)
    return avg

getAverageScore('Joyce Q Kelly')