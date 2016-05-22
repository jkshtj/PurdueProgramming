#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-18 14:19:40 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85533 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab01/line_num.bash $
#$Id: line_num.bash 85533 2016-01-18 19:19:40Z ee364b08 $

if (($# >= 2))
then 
    echo You have provided invalid number of arguments
    exit 1
fi

if [[ ! -r $1 ]]
then 
    echo Cannot read $1
    exit 1
fi
x=1
while read line
do
    echo $x: $line
    ((x=x+1))
done < $1

exit 0
