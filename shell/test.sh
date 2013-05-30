#!/bin/bash

#whoami
#pwd
read -p "Input your birthday date:(MMDD, ex>0709)" birth
now=`date +%m%d`
echo $birth
if [ "$now" == "$birth" ]
then 
echo "Happy birthday to you."
elif [ "$birth" -gt "$now" ]
then 
year=`date +%Y`
total_d=$(($((`date --date="$year$birth" +%s`-`date +%s`))/60/60/24))
elif [ "$birth" -lt "$now" ]
then
year=`date +%Y`
year=$(($year+1))
total_d=$(($((`date --date="$year$birth" +%s`-`date +%s`))/60/60/24))
#echo $year
fi
echo $total_d

