#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-18 13:58:55 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85522 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab01/exit.bash $
#$Id: exit.bash 85522 2016-01-18 18:58:55Z ee364b08 $

while (( $# != 0 ))
do
    if [[ -r $1 ]]
    then
        echo "File $1 is readable!"
    else
        touch $1
    fi
    shift
done 
exit 0
