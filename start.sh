#!/bin/sh
#  Author: Khaled Nakhleh. 2018
# To give permission, type in the terminal: chmod 755 <filename>

function Capturing {
echo "Running ReadCam.py...\n"
python ReadCam.py
}

echo "Running:" $0

if 
test -d camera_1 && test -d camera_2
then
echo "Directories camera_1 and camera_2 exist."
else
echo "Directories camera_1 and camera_2 don't exist. Creating them..."
mkdir camera_1 camera_2
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


