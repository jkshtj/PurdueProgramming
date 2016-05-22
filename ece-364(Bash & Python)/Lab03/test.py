import sys


def getPairwiseDifference(vec):
    if type(vec) is not list:
        return None
    if len(vec) == 0:
        return None
    return [vec[i+1] - vec[i] for i in range(0,len(vec)-1)]


def flatten(l):
    if type(l) is not list:
        return None
    res = [None for x in l if type(x) is not list]
    if len(res) > 0:
        return None
    res = []
    for i in range(0,len(l)):
        x = [value for index, value in enumerate(l[i])]
        res += x
    return res




def partition(l,n):

    return l

def rectifySignal(signal):

    return signal


def floatRange(a,b,s):

    return []


def getLongestWord(sentence):

    return ""

def decodeNumbers(numlist):

    return []

def getCreditCard(s):

    return []