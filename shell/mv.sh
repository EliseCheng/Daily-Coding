#!/bin/bash
for fexec in `find $SRC/C -type f -perm -775`
do
	echo $fexec
	cp $fexec $BIN
done
