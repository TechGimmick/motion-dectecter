import cv2
import numpy as np
import pygame
import time


pygame.mixer.init()
alarm_sound = "alarm.mp3"  # Path to your alarm sound file
alarm_playing = False  # Flag to track if the alarm is playing
black_screen_mode = False  # Flag to track whether the screen is black

def play_alarm():
    global alarm_playing
    if not alarm_playing:
        pygame.mixer.music.load(alarm_sound)
        pygame.mixer.music.play(-1)
        alarm_playing = True

def stop_alarm():
    global alarm_playing
    if alarm_playing:
        pygame.mixer.music.stop()
        alarm_playing = False

def detect_motion():
    global black_screen_mode
    cap = cv2.VideoCapture(0)
    time.sleep(2)

    ret, frame1 = cap.read()
    gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_frame1 = cv2.GaussianBlur(gray_frame1, (21, 21), 0)

    while cap.isOpened():
        ret, frame2 = cap.read()
        if not ret:
            break

        gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray_frame2 = cv2.GaussianBlur(gray_frame2, (21, 21), 0)
        diff_frame = cv2.absdiff(gray_frame1, gray_frame2)
        _, thresh = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)


        thresh = cv2.dilate(thresh, None, iterations=2)


        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False


        if black_screen_mode:
            display_frame = np.zeros_like(frame2)
        else:
            display_frame = frame2.copy()

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

            motion_detected = True


            if black_screen_mode:
                cv2.drawContours(display_frame, [contour], -1, (255, 255, 255), 2)  # White contour
            else:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        if motion_detected and black_screen_mode:
            play_alarm()
            print("Alarm")
        else:
            stop_alarm()
        cv2.imshow("Motion Detection", display_frame)


        gray_frame1 = gray_frame2
        key = cv2.waitKey(1) & 0xFF
        if key == ord('t'):
            black_screen_mode = not black_screen_mode

        if key == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    stop_alarm()

if __name__ == "__main__":
    detect_motion()
