import sys
import glob
import re
import os

def rowSumIsValid(mat):
    sum_mat_row = sum(mat[0])
    for row in mat:
       if sum_mat_row == sum(row):
           continue
       else:
           return False

    return True

def columnSumIsValid(mat):
    n = len(mat[0])
    col_sum = zip(*mat)
    col_sum = list(col_sum)
    col_mat_sum = sum(col_sum[0])
    for col in col_sum:
        if col_mat_sum == sum(col):
            continue
        else:
            return False

    return True

def magicSquareIsValid(filePath):
    mat = []
    with open(filePath,'r') as f:
        for line in f:
            row = re.findall('[0-9]+',line)
            for i in range(len(row)):
                row[i] = int(row[i])
            mat.append(row)
    if rowSumIsValid(mat) & columnSumIsValid(mat):
        return True

    return False

def getTotalCost(itemSet):
    name=itemSet[0]
    price=itemSet[1]

    file_list = glob.glob('Stores/*.txt')
    for file in file_list:
        with open(file,'r') as f:
            f.readline()
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