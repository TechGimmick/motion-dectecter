Motion Detection Alarm System
A Python-based security application that uses a webcam to detect motion. When motion is detected while in "Black Screen Mode," the system triggers an audible alarm.

Description
This script captures video from your computer's webcam and analyzes consecutive frames to identify movement. In its standard mode, it visually highlights motion by drawing green rectangles around moving objects.

For a more practical security application, you can toggle "Black Screen Mode." In this mode, the video feed is blacked out, but the script continues to detect motion in the background. If movement is detected, it outlines the motion in white and triggers a loud, continuous alarm sound.

Features
Real-time Motion Detection: Captures and processes the webcam feed live.

Visual Feedback: Draws rectangles around detected objects in the standard view.

Black Screen (Alarm) Mode: A discreet mode that blacks out the screen and sounds an alarm when motion is detected.

Simple Keyboard Controls: Easily toggle modes or quit the application.

Customizable Alarm: You can use any MP3 file as the alarm sound.

Requirements
To run this script, you will need Python 3 and the following libraries:

opencv-python

numpy

pygame

You can create a requirements.txt file with the following content:

opencv-python
numpy
pygame

Installation
Clone the repository or download the script.

Install the required libraries:
Open your terminal or command prompt and run:

pip install -r requirements.txt

Or install them manually:

pip install opencv-python numpy pygame

Add an alarm sound:

Find an MP3 audio file you want to use as an alarm.

Save it in the same directory as the Python script.

Rename the file to alarm.mp3 or update the alarm_sound variable in the script to your file's name.

Usage
Make sure your webcam is connected and uncovered.

Run the script from your terminal:

python motion_detector.py

(Assuming you've named the file motion_detector.py)

A window will appear showing your webcam feed.

Keyboard Controls
t Key: Press t to toggle between the standard visual mode and the "Black Screen" alarm mode.

q Key: Press q while the video window is active to stop the script and close the application.
