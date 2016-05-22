#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-02-16 15:19:17 -0500 (Tue, 16 Feb 2016) $
#$Revision: 88255 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Lab05/scheduler.bash $
#$Id: scheduler.bash 88255 2016-02-16 20:19:17Z ee364b08 $

if (($# != 1))
then 
    echo You have provided invalid number of arguments
    exit 1
fi

if [[ ! -e $1 ]]
then 
    echo Input file $1 does not exist
    exit 2
fi

if [[ -e "schedule.out" ]]
then
    echo "schedule.out already exists"
    rm "schedule.out"
    exit 3
fi


#Declarations#
ppl_avl=0   #num of ppl available at a given time
max_time=0  #time at which most people are available
time_list=(07:00 08:00 09:00 10:00 11:00 12:00 12:00 14:00 15:00 16:00 17:00)
name_list=$(cut -d' ' -f1 $1)  #name list of ppl
tim_flag=0
IFS=','

exec 3<$1 #creating file descriptor for input file
exec 4>"schedule.out"

for (( i=0; i<12; i++ ))
do
    printf "\t${time_list[$i]}" >&4
done

printf "\n" >&4

while read -a line <&3
do
    time_list=$(echo $line | sort)
    echo $time_list
    printf "$name\t" >&4

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="07:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="08:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="09:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="10:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="11:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="12:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="13:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="14:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="15:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="16:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi

    for time in t7 t8 t9 t10 t11 t12 t13 t14 t15 t16 t17
    do
        if [[ $time="17:00" ]]
        then
            printf "Y\t" >&4
	    tim_flag=1
	    break
	fi
    done
    
    if (( tim_flag != 1))
    then
	printf "-\t" >&4
    else
	tim_flag=0
    fi
    printf "\n" >&4    

done
    
exit 0
