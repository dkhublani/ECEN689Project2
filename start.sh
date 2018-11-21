#!/bin/sh
#  Author: Khaled Nakhleh. 2018
# To give permission, type in the terminal: chmod 755 <filename>

echo "Running:" $0

echo "Making/overwriting directories for saving pictures ...\n"

mkdir camera_1
mkdir camera_2

echo "Running ReadCam.py...\n"
python ReadCam.py

exit
