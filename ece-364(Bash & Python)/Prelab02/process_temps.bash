#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-25 03:13:04 -0500 (Mon, 25 Jan 2016) $
#$Revision: 86690 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab02/process_temps.bash $
#$Id: process_temps.bash 86690 2016-01-25 08:13:04Z ee364b08 $

#Error checking for different parameters#
if (($# != 1))
then 
    echo "Usage : process_temps.bash <input file>"
    exit 1
fi

if [[ ! -r $1 ]]
then 
    echo "Error: $1 is not a readable file."
    exit 2
fi

#Declarations#
time_val=0
avg=0
count=0
sum=0
flag=0

exec <$1 #creating a file descriptor b/c we need to start reading from the second line of the file

while read line<&0
do
    if ((flag == 0))
    then 
        read line <&0
        flag=1
    fi

    if ((flag == 1))
    then
        arr=($line)
        time_val=${arr}
        for ((i=1; i<${#arr[*]}; i++))
        do
            ((sum=sum+${arr[i]}))
            ((count=count+1))
        done
        ((avg=sum/count))
        echo "Average temperature for time $time_val was $avg C."
    fi
done

exit 0
