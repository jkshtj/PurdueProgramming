#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-18 20:41:11 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85859 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab01/sensor_sum.sh $
#$Id: sensor_sum.sh 85859 2016-01-19 01:41:11Z ee364b08 $

if (($# > 1))
then 
    echo You have provided invalid number of arguments
    exit 1
fi

if [[ ! -r $1 ]]
then 
    echo Cannot read $1!
    exit 1
fi


while read line
do
    s_id=$(echo $line | cut -d' ' -f1)
    new_id=$(echo $s_id | cut -d'-' -f1) 
    
    s1=$(echo $line | cut -d' ' -f2)
    s2=$(echo $line | cut -d' ' -f3)
    s3=$(echo $line | cut -d' ' -f4)

    ((sum=s1+s2+s3))
    echo $new_id $sum
done < $1

exit 0
