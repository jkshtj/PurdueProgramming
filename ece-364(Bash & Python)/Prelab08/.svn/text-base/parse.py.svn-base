import os
import sys
import math


def parse_file(filename):
    ## opening the file
    try:
        f = open(filename,'r')
    except IOError:
         sys.stderr.write('%s is not a readable file or it does not exist\n' % filename)
         sys.exit(1)

    ## now continue reading file
    #f = open('exp.data','r')

    all_lines = f.readlines()
    head = all_lines[0]
    num_list=[]
    comment=[]
    for line in all_lines[1:]:
        line = line.split()
        for x in line:
            try:
                num_list.append(int(x))
            except ValueError:
                comment.append(x) ## in case of a value error, append x to the comment list

        sys.stdout.write('%0.3f %s\n' %(sum(num_list)/len(num_list)," ".join(comment)))
        num_list=[]
        comment=[]

    sys.exit(0)

def main():
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: parse.py [filename]\n')
        sys.exit(1)

    filename = sys.argv[1]
    parse_file(filename)
if __name__ == "__main__" :
    main()