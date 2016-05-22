import os
import sys
import math

def find_median(l1,l2):
    median = 0
    result=[]
    result=l1+l2
    result = sorted(result)
    if len(result) % 2 == 0:
        median = math.floor((len(result) - 1)/2)
    else:
        median = (len(result) - 1)/2
    return (result[median],result)