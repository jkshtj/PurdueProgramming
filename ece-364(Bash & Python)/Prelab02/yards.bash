#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-25 00:14:36 -0500 (Mon, 25 Jan 2016) $
#$Revision: 86674 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab02/yards.bash $
#$Id: yards.bash 86674 2016-01-25 05:14:36Z ee364b08 $


#Error checking for usage of script and readibility of the input file#
if (($# != 1))
then 
    echo "Usage: yards.bash <filename>"
    exit 1
fi

if [[ ! -r $1 ]]
then 
    echo Error: $1 is not readable
    exit 1
fi

#Declarations#
sum=0 #keeps track of the sums of the yards of each team
count=0 #number of teams in each conference
avg=0 #avg yardage per team
max_yardage=0 #largest avg yardage in all the conferences
var=0 #variance in yardage per conference

while read line
do
    arr=($line)
    for i in ${!arr[*]}
    do
        if ((i==0))
        then
            school_name=${arr[i]}
        else
            ((sum=sum+${arr[i]}))
            ((count=count+1))
            ((avg=sum/count))
        fi
    done

    for ((i=1; i<=${#arr[*]}-1; i++))
    do
        (( var=var + (( ${arr[i]} - $avg)*(${arr[i]} - $avg )) ))
    done

    if ((avg>max_yardage))
    then 
        max_yardage=$avg
    fi
    
    ((var=var/count))
    
    echo $school_name schools averaged $avg yards receiving with a variance of $var
    
    #Reassigning all the variables
    sum=0
    count=0
    avg=0
    var=0
done<$1

echo The largest average yardage was $max_yardage

exit 0
