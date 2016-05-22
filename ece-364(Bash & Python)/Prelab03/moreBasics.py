import sys

def getAverage(l):
    sum_l = sum(l)
    avg_l = sum / len(l)
    return avg_l

def getHeadAverage(l,n):
    sum_n  = sum(l[0:n])
    avg_n = sum/n
    return avg_n

def getTailMax(l,m):
    max_val = max(l[m:])
    return max_val

def getNumberAverage(l):
    res = []
    [res.append(x) for x in l if type(x) is int or type(x) is float]
    sum_res = sum(res)
    return sum_res/len(res)

def getFormattedSSN(n):
    pad = 0
    n = str(n)
    l = []
    a = []
    if (len(n) < 9):
        pad = 9 - len(n)

    if pad != 0:
        str = '%0*d' % (pad,0)
        a += str  ##padding the res char array with zeroes if len(n) != 9

    a += n
    l.append(a[0])
    l.append(a[1])
    l.append(a[2])
    l.append('-')
    l.append(a[3])
    l.append(a[4])
    l.append('-')
    l.append(a[5])
    l.append(a[6])
    l.append(a[7])
    l.append(a[8])

    fin_str = "".join(l)
    return fin_str

def findName(l,s):
    new_str = [str for str in l if s in str]
    return new_str

def getColumnSum(mat):
    num_col = len(mat[0]) ## number of columns in the matrix
    arr=[]
    arr[0:num_col] = zip(*mat)
    res=[]
    res=map(sum,arr)
    return res

def getFormattedNames(ln):
    res = ['{0}, {1} {2}.'.format(last,first,mi) for first, mi, last in ln]
    return res

def getElementwiseSum(l1,l2):
    if(len(l1) > len(l2)):
        temp = l1[len(l1)-len(l2)+1:]
        l1 = [sum(x) for x in zip(l1,l2)]
        return l1+temp
    else:
        temp = l2[len(l2)-len(l1)+1:]
        l2 = [sum(x) for x in zip(l1,l2)]
        return l2+temp

def removeDuplicates(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp

def getMaxOccurence(l):
    max_cnt = 0
    max_char = 0
    for x in l:
        if max_cnt < l.count(x):
            max_cnt = l.count(x)
            max_char = x
    return max_char

def getMaxProduct(l):
    i = 0
    max_prod = 0
    while i < len(l) - 4:
        prod = l[i]*l[i+1]*l[i+2]
        if max_prod < prod:
            max_prod = prod
    return max_prod
