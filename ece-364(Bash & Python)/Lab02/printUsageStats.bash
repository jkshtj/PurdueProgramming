#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-26 15:31:34 -0500 (Tue, 26 Jan 2016) $
#$Revision: 86959 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Lab02/printUsageStats.bash $
#$Id: printUsageStats.bash 86959 2016-01-26 20:31:34Z ee364b08 $

if (($# != 1))
then 
    echo You have provided invalid number of arguments
    exit 1
fi

if [[ ! -e $1 ]]
then 
    echo Input file $1 does not exist
    exit 1
fi

#Declarations#
time_stamp=0
choice=0
nusers=0
N=0
user_id=0
usage=0
mem=0
PID=0
rtime=0
com=0

exec 3<$1 #creating file descriptor for input file

read line <&3 #reading top line
time_stamp=$(echo $line | cut -d',' -f1)
time_stamp=$(echo $time_stamp | cut -d' ' -f3)

nusers=$(echo $line | cut -d',' -f3)
nusers=$(echo $nusers | cut -d' ' -f1)

tail -n +8 $1>out.txt # copy useful line to another file

echo Parsing file "$1". Timestamp: $time_stamp
echo Your choices are:
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N highest mem usages"
echo "4) Top three longest running processes"
echo "5) All processes by a specific user"
echo "6) Exit"

read -p "Please enter your choice: " choice

while ((choice != 6))
do
    if ((choice == 1))
    then 
        echo "Total number of active user IDs: $nusers"
    elif((choice == 2))
    then
        read -p "Enter a value for N: " N
        exec 4<out.txt
        sort -r -n -k9 out.txt>out2.txt
        exec 4<out2.txt

        for ((i=1; i<=$N; i++))
        do
            read line <&4
            user_id=$(echo $line | cut -d' ' -f2)
            usage=$(echo $line | cut -d' ' -f9)
            echo "User $user_id is utilizing CPU resources at $usage %"
        done
    elif ((choice == 3))
    then
        read -p "Enter a value for N :" N
        exec 4<out.txt
        sort -r -n -k10 out.txt >out2.txt 
        exec 4<out2.txt

        for ((i=1; i<=$N; i++))
        do
            read line <&4
            user_id=$(echo $line | cut -d' ' -f2)
            mem=$(echo $line | cut -d' ' -f10)
            echo "User $user_id is utilizing men resources at $mem %"
        done
    elif ((choice == 4))
    then
        exec 4<out.txt
        sort -r -n -k11 out.txt >out2.txt
        exec 4<out2.txt

        for ((i=1; i<=3; i++))
        do
            read line <&4
            PID=$(echo $line | cut -d' ' -f1)
            com=$(echo $line | cut -d' ' -f12)
            echo "PID: $PID, cmd: $com"
        done
    elif ((choice == 5))
    then
        read -p "Please enter a valid username: " username
        grep "$username" out.txt >out1.txt 
        if (($? != 0))
        then 
            echo "No match found"
        else
            exec 5<out1.txt

            while read line <&5
            do
                com=$(echo $line | cut -d' ' -f12)
                usage=$(echo $line | cut -d' ' -f9)
                echo "$usage $com"
            done
        fi       
    else
        exit 0
    fi

    read -p "Please enter your choice: " choice
done

exit 0
