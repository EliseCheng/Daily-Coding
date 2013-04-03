#!/bin/sh

OUTPUT="/home/alice/Online/output.txt"
touch $OUTPUT
echo "start to search..."
searchFolder()
{
	cd $1
	for filename in `ls`
	do
  	if [ -f $filename ] 
		then
  	  echo $filename >> $OUTPUT
  	  grep "project" *.xml >> $OUTPUT 
  	  echo "=============================" >> $OUTPUT
  	elif [ -d $filename ]
		then
			#echo "sub--$1"
			searchFolder $filename
		fi
	done
	cd ../
}

echo "..." >> $OUTPUT
searchFolder www

echo "Finished, the result is saved in $OUTPUT"




