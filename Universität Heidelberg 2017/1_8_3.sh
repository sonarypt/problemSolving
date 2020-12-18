#!/bin/bash

DIR="../bash-course-2017_final/resources/matrices/"

# find line contains the word "hunger" and the second line contains the word "soon"

< ${DIR}3.mtx tail -n +2 | cut -f 3 -d " " | sort -u | wc -l
