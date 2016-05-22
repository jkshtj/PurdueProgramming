import os
import sys
import math
from listmod import *

list1=[]
list2=[]

list1 = input('\nEnter the first list of numbers: ')
list2 = input('Enter the second list of numbers: ')
list1=list1.replace(' ',', ')
list2=list2.replace(' ',', ')

print('First list: [' + str(list1)+']')
print('Second list: [' + str(list2)+']')

list1 = [int(x) for x in list1.split(', ')]
list2 = [int(x) for x in list2.split(', ')]

(med,res) = find_median(list1,list2)

print('Merged List: ' + str(res))
print('Median: '+ str(med))