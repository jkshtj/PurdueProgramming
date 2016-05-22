#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-19 11:34:09 -0500 (Tue, 19 Jan 2016) $
#$Revision: 86126 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab01/svncheck.bash $
#$Id: svncheck.bash 86126 2016-01-19 16:34:09Z ee364b08 $


if (($# > 0))
then 
    echo "You have provided invalid number of arguments"
    exit 1
fi

while read line
do
   checker=$(svn status $line | head -c1)
   fname=$line 
   
   #if the file is not in svn, exists and is not executable
   if [[  $checker != "" && -e $fname && ! -x $fname ]]
   then
       
       echo "Would you like to make $fname executable?(y/n)"
       read ans
       if [[ $ans == y ]]
       then
            chmod +x $fname
       fi
   svn add $fname
   
   #if the file is in svn but is not executable
   elif [[ $checker == "" && -e $fname && ! -x $fname ]]
   then
       svn propset svn:executable ON $fname
   fi
   
   #if the file is not in svn and does not exist
   if [[ $checker == "" && ! -e $fname ]]
   then
      if [[ ! -e $fname ]]
       then
           echo "Error: File $fname appears to not exist"
       fi
   fi  
done < file_list

svn commit -m "Auto-committing code"

exit 0
