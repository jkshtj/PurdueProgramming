#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-19 15:22:31 -0500 (Tue, 19 Jan 2016) $
#$Revision: 86204 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Lab01/getFinalScores.bash $
#$Id: getFinalScores.bash 86204 2016-01-19 20:22:31Z ee364b08 $


file=$@
outfile=$(echo $file | cut -d'.' -f1)
outfile=$outfile.out
if (($# != 1))
then 
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
fi

if [[ ! -e $1 && ! -r $1 ]]
then 
    echo "Error reading input file: $file"
    exit 2
fi

if [[ ! -e $outfile ]]
then
    while read line
    do
        name=$(echo $line | cut -d',' -f1) 
        s1=$(echo $line | cut -d',' -f2)
        s2=$(echo $line | cut -d',' -f3)
        s3=$(echo $line | cut -d',' -f4)
        s4=$(echo $line | cut -d',' -f5)

        ((final_score=15*s1/100 + 30*s2/100 + 30*s3/100 + 25*s4/100))
        printf "$name $name2, $final_score\n" >> $outfile   
    done < $1
else
    echo "Output file $outfile already exists."
    exit 3
fi

exit 0
