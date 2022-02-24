import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\student\Downloads\one-by-one-person-detection.mp4')
cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)

while True:
    ret_val, frame = cap.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
