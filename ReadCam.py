#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:00:32 2018

Name: khalednakhleh

Frames' sorting script file
"""

import cv2

# numbers in VideoCapture here specifies which camera is being used.
# For two external cameras, 0 and 2 worked.

def capture(obstacle, Run):
    cap_1 = cv2.VideoCapture(0)
    cap_2 = cv2.VideoCapture(1)  
    FrameCount = 0
    
    while(True):
        print("number of generated frames: " + str(FrameCount))
        # Capturing frames from two cameras
        ret, frame_1 = cap_1.read()
        ret, frame_2 = cap_2.read()
        
        # Graying frames
        
        gray_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
        gray_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
        FileName = "run_" + str(Run) + "_frame_" + str(FrameCount)
        if (obstacle.lower() == "y"):
            FileName_1 = "obs_1/" + FileName + ".jpg"
            FileName_2 = "obs_2/" + FileName + ".jpg"
            cv2.imwrite(FileName_1, gray_1)
            cv2.imwrite(FileName_2, gray_2)
        
        else:
            FileName_1 = "no_obs_1/" + FileName + ".jpg"
            FileName_2 = "no_obs_2/" + FileName + ".jpg"
            cv2.imwrite(FileName_1, gray_1)
            cv2.imwrite(FileName_2, gray_2)
        
        # If we want a frame preview window, uncomment the following lines
        
        #cv2.imshow('frame',gray_1)
        #cv2.imshow('frame',gray_2)
        
        FrameCount += 1
        
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    # Releasing capture
    cap_1.release()
    cap_2.release()
    cv2.destroyAllWindows()
    
def main():

    obstacle = input("For storing in the obstacles' directories type 'y' or 'Y'. For no obstacles, type anything else: ")
    Run = input("\nEnter run count: ")
    capture(obstacle, Run)


if __name__ == "__main__":
    main()
    
