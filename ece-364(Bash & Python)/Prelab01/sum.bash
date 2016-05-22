#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-18 13:19:09 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85507 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab01/sum.bash $
#$Id: sum.bash 85507 2016-01-18 18:19:09Z ee364b08 $

sum=0
while (($# != 0))
do
    #((X=X+1))
    ((sum=sum+$1))
    shift
done
echo The sum is:$sum

exit 0
