#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:53:51 2024

@author: umitsen
"""

import cv2
import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--step",default=1,type=int)
args = parser.parse_args()

def extractFrames(vid,stepFrame):
    vidName = vid.split(".")[0]
    os.makedirs(vidName,exist_ok=True)
    capture = cv2.VideoCapture(vid)
    totalFrameCount = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    extractedFrames = 0
    for i in range(0,totalFrameCount,stepFrame):
        if capture.isOpened():
            ret, frame = capture.read()
            if ret == False:
                break
            else:
                formatCount = str(i+1).zfill(len(str(totalFrameCount)))
                cv2.imwrite(f"{vidName}/{formatCount}.jpg", frame)
                extractedFrames +=1
                print(f"Completed : {formatCount} / {totalFrameCount}",end="\r",flush=True)
    print(f"Finish : {vidName} {extractedFrames} / {totalFrameCount}")


os.makedirs("completed_videos",exist_ok=True)
for vid in os.listdir("."):
    if vid.endswith((".mp4",".mov",".MP4",".MOV")):
        extractFrames(vid,args.step)
        shutil.move(vid, "completed_videos")
        print(f"Moved : {vid}")
        


