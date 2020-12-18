#!/bin/bash

# at least one pipe
# < ../bash-course-2017_final/resources/gutenberg/pg74.txt grep hunger | wc -l

# use no pipe at all
< ../bash-course-2017_final/resources/gutenberg/pg74.txt grep -c hunger
