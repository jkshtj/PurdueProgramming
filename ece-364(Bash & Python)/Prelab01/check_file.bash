#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-18 16:35:47 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85617 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab01/check_file.bash $
#$Id: check_file.bash 85617 2016-01-18 21:35:47Z ee364b08 $

if (($# >= 2))
then 
    echo You have provided invalid number of arguments
    exit 1
fi

if (($# == 0))
then
echo "Usage: ./check_file.bash <filename>"
exit 1
fi

if [[ -e $1 ]]
then 
    echo $1 exists
else
    echo $1 does not exist
fi

if [[ -d $1 ]]
then 
    echo $1 is a directory
else
    echo $1 is not a directory
fi

if [[ -f $1 ]]
then 
    echo $1 is an ordinary file
else
    echo $1 is not an ordinary file
fi

if [[ -r $1 ]]
then 
    echo $1 is readable 
else
    echo $1 is not readable
fi

if [[ -w $1 ]]
then 
    echo $1 is writable
else
    echo $1 is not writable
fi

if [[ -x $1 ]]
then 
    echo $1 is executable
else
    echo $1 is not executable
fi

exit 0
