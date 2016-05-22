#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-19 19:17:18 -0500 (Tue, 19 Jan 2016) $
#$Revision: 86289 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Lab01/getCourseStats.bash $
#$Id: getCourseStats.bash 86289 2016-01-20 00:17:18Z ee364b08 $

input=$@

if (($# != 1))
then 
    echo "Usage: ./getCourseStats.bash <course name>"
    exit 1
fi

if [[ $input != "ece364" && $input != "ece337" && $input != "ece468" ]]
then 
    echo "Error course $input is not a valid option."
    exit 5
fi

files=$(ls gradebooks/$input*.txt)

for file in $files
do
    getFinalScores.bash $file
    if (($? != 0))
    then
        echo "Error while running getFinalScores.bash"
        exit 3
    fi
done
    
count=0
tot=0
max=0

files=$(ls gradebooks/$input*.out)

for file in $files
do
    scores=$(cut -d',' -f2 $file)
    for score in $scores
    do
        ((tot=$score+$tot))
        ((count=$count+1))
        if (($score > $max))
        then
            ((max=score))    
        fi 
    done
done


for file in $files
do
    while read name1 name2 comma score
    do
        if (($score == $max))
        then 
            name1_tp=$name1
            name2_tp=$name2
        fi
    done < $file 

done

((avg=$tot/$count))

echo Total students: $count 
echo Average score: $avg
echo $name1_tp $name2_tp has the highest score of $max

rm gradebooks/$input*.out
exit 0
