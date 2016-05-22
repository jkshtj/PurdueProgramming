#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-25 02:31:52 -0500 (Mon, 25 Jan 2016) $
#$Revision: 86684 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Prelab02/run.bash $
#$Id: run.bash 86684 2016-01-25 07:31:52Z ee364b08 $


#Error checking for number of arguments, readibility of file and if the output file already exists#
if (($# != 2))
then 
    echo You have provided invalid number of arguments
    exit 1
fi

if [[ ! -r $1 ]]
then 
    echo Cannot read $1
    exit 1
fi

if [[ -e $2 ]]
then 
    read -p "$2 exists. Would you like to delete it?" ans
    if [[ $ans = "y" ]]
    then 
        rm $2 2>/dev/null                
    else
        read -p "Enter a new filename: " ans
        $2=$ans
    fi
fi 

#Declarations#
cache=(1 2 4 8 16 32)
i_width=(1 2 4 8 16)
p_name=0
c_size=0
isu_width=0
cpi=0
e_time=0
min_e_time=10000

    for i in ${cache[*]}
    do
        for j in ${i_width[*]}
        do
            rm quick_sim 2>/dev/null #removing existing quicksim binary

            if ! gcc $1 -o quick_sim
            then
                echo ERROR: quick_sim could not be compiled!
                exit 1
            fi

            for k in a i
            do
                line=$(quick_sim $i $j $k) #output to be redirected to the output file specified 
                p_name=$(echo $line | cut -d':' -f2)
                c_size=$(echo $line | cut -d':' -f4)
                isu_width=$(echo $line | cut -d':' -f6)
                cpi=$(echo $line | cut -d':' -f8)
                e_time=$(echo $line | cut -d':' -f10)
                echo "$p_name:$c_size:$isu_width:$cpi:$e_time">>$2

                if ((e_time < min_e_time))
                then 
                    min_e_time=$e_time
                    a=$p_name
                    b=$c_size
                    c=$isu_width
                fi
            done
        done
    done
    echo "Fastest run time achieved by $a with cache size $b and issue width $c was $min_e_time"

exit 0
