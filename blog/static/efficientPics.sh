#!/bin/bash

DIR=$(pwd);
for i in $(find $DIR -type f \( -name "*.jpg" -or -name "*.jpeg" -or -name "*.JPG" \)); do
    echo "${BOLD}OPTIMIZING ${NORM}: $i ..."
    echo "${BOLD}OLD${NORM}:" $(du -h $i | cut -f1 )
    jpegtran -copy comments -optimize -progressive -outfile $i $i
    jpegrescan -s -a -q $i $i
    jpegoptim -q -t -o 4 -s -m95 "$i"
    echo "${BOLD}NEW${NORM}:" $(du -h $i | cut -f1 )
    echo
done 
