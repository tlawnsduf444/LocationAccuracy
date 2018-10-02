# coding=utf8

import cv2
from ar_markers import detect_markers
from datetime import datetime

if __name__ == '__main__':
    print('Press "q" to quit')
    capture = cv2.VideoCapture(1)
    filename = datetime.now().strftime('%H%M%S') + "Accurancy.txt"
    with open(filename, "a") as f:
        f.write("Time"+ '\t' + "Location" + '\n')
    moving_list = []
    flag = False

    if capture.isOpened():  # try to get the first frame
        frame_captured, frame = capture.read()
    else:
        frame_captured = False

    while frame_captured:
        markers = detect_markers(frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        
        if key == ord('s'):
            with open(filename, "a") as f:
                f.write(datetime.now().strftime('%H:%M:%S') + '\t' + str(marker.center) + '\n')
            moving_list.append([marker.center,'Blue'])

        for marker in markers:
            marker.highlite_marker(frame)
            moving_list.append([marker.center,'Red'])
        
        for position in moving_list:
            if position[1] == 'Red': 
                frame = cv2.circle(frame, (position[0][0],position[0][1]), 5, (0,0,255), -1)

        for position in moving_list:
            if position[1] == 'Blue': 
                frame = cv2.circle(frame, (position[0][0],position[0][1]), 5, (255,0,0), -1)
                
        cv2.imshow('Test Frame', frame)
        frame_captured, frame = capture.read()

    capture.release()
    cv2.destroyAllWindows()
