#!/bin/bash
i=0
str=""
while [ $i -lt 9 ]
do
	str="$i$str"
	echo $str
	i=$(($i+1))
done


read op1 op2 op3

case $op2 in
	+ )
		echo "#############"
		echo $(($op1 + $op3))
	;;
	/ )
		if [ "$op3" == "0" ]
		then
			echo "zero is invalid"
		fi
	;;
	* )
		echo "invalid operation"
	;;
esac
#echo $y 
