import sys
import glob
import re
import os


def getWordFrequency():
    freq_list = {}
    file_list = []
    word_list = []
    file_list = glob.glob('../Prelab04/files/*.txt')

    for file in file_list:  ## accessing each file from the list of files
        with open(file, 'r') as f:  ## opening the curr file
            all_lines = f.readlines()  ## reading the whole file
            for line in all_lines:  ## reading one line at a time from all_lines
                word_list = re.findall("[A-Za-z0-9\']+", line)  ## splitting the line into words
                for word in word_list:  ## accessing each line word by word
                    if word not in freq_list:
                        freq_list[word] = 1  ## if word not found, insert it into the dict
                    else:
                        freq_list[word] = freq_list.get(word) + 1  ## else inc freq by 1

    # print (freq_list)
    return freq_list


#################################################################################

def getDuplicates():
    file_group = {}
    final = {}
    unique_wl = []
    file_list = []
    fnames = []

    file_list = glob.glob('../Prelab04/files/*.txt')

    for file in file_list:  ## accessing each file from the list of files
        bname = os.path.basename(file).split('.')[0]  ## extracting the base file name
        with open(file, 'r') as f:  ## opening the curr file
            all_lines = f.read()  ## reading the whole file

            if all_lines in file_group:
                fnames.append(bname)
                file_group[all_lines] = file_group.get(all_lines) + fnames
                fnames = []
            else:
                fnames.append(bname)
                file_group[all_lines] = fnames
                fnames = []

    for key, value in file_group.items():
        value.sort()
        key = key.replace(",","")
        key = key.replace(".","")
        key = key.replace(",","")

        unique_wl = key.split()
        unique_set = set(unique_wl)
        final[value[0]] = (len(unique_set), value)
    #print(final)
    return final


getDuplicates()


###################################################################################

def getPurchaseReport():
    trans = {}  ## transaction dictionary
    ledger = {}  ## stores item name and cost
    file_list = []
    cost = 0
    total_cost = 0

    ## first we will get a list of all items that are available
    with open('../Prelab04/purchases/Item List.txt', 'r') as f:  ## opening the curr file
        f.readline()  ## first 2 lines of no use
        f.readline()
        for line in f:
            item = re.findall('[A-Za-z]+', line)[0]
            cost = float(re.findall('[0-9]+\.[0-9]+', line)[0])
            ledger[item] = cost

    file_list = glob.glob('../Prelab04/purchases/purchase_*.txt')

    for file in file_list:
        pid = re.split('_|\.', os.path.basename(file))[1][2]  ## this is the transaction id
        with open(file, 'r') as f:  ## opening the curr file
            f.readline()  ## these two lines are of no interest to us
            f.readline()
            print(pid + "##############################################")
            for line in f:
                item = re.findall('[A-Za-z]+', line)[0]
                total_cost += int(re.findall('\d+', line)[0]) * ledger.get(item)
        trans[int(pid)] = round(total_cost, 2)  ## storing pid and cost in the dict
        total_cost = 0

    print(trans)
    return trans


####################################################################################

def getTotalSold():
    ledger = {}
    file_list = []
    num_sold = 0

    ## first we will get a list of all items that are available
    with open('../Prelab04/purchases/Item List.txt', 'r') as f:  ## opening the curr file
        f.readline()  ## first 2 lines of no use
        f.readline()
        for line in f:
            key = re.findall('[A-Za-z]+', line)[0]
            ledger[key] = 0

        ## Now we will read the purchase file
        file_list = glob.glob('../Prelab04/purchases/purchase_*.txt')

        for file in file_list:
            with open(file, 'r') as f:  ## opening the curr file
                f.readline()  ## these two lines are of no interest to us
                f.readline()
                for line in f:
                    item = re.findall('[A-Za-z]+', line)[0]
                    num_sold = int(re.findall('\d+', line)[0])
                    ledger[item] = ledger.get(item) + num_sold

    return ledger
