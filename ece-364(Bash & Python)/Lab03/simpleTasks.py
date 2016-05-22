import sys


def getPairwiseDifference(vec):
    res = []
    if type(vec) is not list:
        return None
    if len(vec) == 0:
        return None
    for i in range(0,len(vec)):
        if i+1 < len(vec):
            res.append(vec[i+1] -vec[i])
    return res



def flatten(l):
    res = []
    if type(l) is not list:
        return None
    for x in l:
        if type(x) is not list:
            return None

    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            res.append(l[i][j])

    return res



def partition(l,n):
    if type(l) is not list:
        return None
    if len(l) == 0:
        return None

    res = []
    k = 0
    j = n
    while j <= len(l):
        res.append([l[i] for i in range(k,len(l)) if l.index(l[i]) < j])
        k = j
        j += n
    if k < len(l):
        res.append(l[k:])
    return res



def rectifySignal(signal):
    if type(signal) is not list:
        return None
    if len(signal) == 0:
        return None
    for i in range(0,len(signal)):
        if signal[i] < 0:
            signal[i] = 0
    return signal



def floatRange(a,b,s):
    if a >= b:
        return None
    x = a
    res=[]
    res.append(round(a,1))
    while round(x+s,1) < b:
        res.append(round(x+s,1))
        x=x+s
    res.append(round(b,1))
    return res



def getLongestWord(sentence):
    if type(sentence) is not str:
        return None
    res = sentence.split(" ")

    if len(res) is 1:
        return None

    max_word= "a"
    for word in res:
        if len(max_word) < len(word):
            max_word = word
    return max_word



def decodeNumbers(numlist):
    if type(numlist) is not list:
        return None
    for i in range(0,len(numlist)):
        if type(numlist[i]) is not int:
            return None
    for i in range(0,len(numlist)):
        numlist[i] = chr(numlist[i])
    str = "".join(numlist)
    return str



def getCreditCard(s):
    if len(s) == 0:
        return None
    i = 0
    r = []
    r = list(s)
    while i < len(r):
        n=r[i]
        if ord(r[i]) < 48 or ord(r[i]) > 57:
            del r[i]
            i -= 1
        i += 1
    res = []
    for x in r:
        res.append(int(x))
    return res
