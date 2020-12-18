#!/bin/bash

DIR="../bash-course-2017_final/resources/gutenberg/"

# find line contains the word "hunger" and the second line contains the word "soon"

< ${DIR}pg74.txt tail -n +2
