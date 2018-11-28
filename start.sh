#!/bin/sh
#  Author: Khaled Nakhleh. 2018
# To give permission, type in the terminal: chmod 755 <filename>

function Capturing {
echo "Running ReadCam.py...\n"
python ReadCam.py
}

echo "Running:" $0


if test -d "chair_1" && test -d "chair_2" && test -d "no_obs_1" && test -d "no_obs_2";
then
echo "All directories exist."
else
echo "Some or all directories don't exist. Creating them..."
mkdir chair_1 chair_2 no_obs_1 no_obs_2
fi

valid=0
echo "Start capturing? [y/n]"

while 
[ $valid == 0 ]
do 
read ans
case $ans in 
yes|YES|y|Y|yup|YUP) 
             echo "Starting..."
             Capturing
             valid=1;;
no|NO|n|N|nope|NOPE)
            echo "Shutting down..."
            valid=1
            exit;;
*           )
            echo "type yes or no in any form";;
esac
done
