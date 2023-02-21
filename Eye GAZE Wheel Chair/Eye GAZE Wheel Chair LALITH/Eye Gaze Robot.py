import cv2
from gaze_tracking import GazeTracking
import pyautogui as pag
from time import sleep
import serial


print("Libraries updated")
#sleep(0)




pag.FAILSAFE = False
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
text = ""
text_old = ""


while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    frame = cv2.flip(frame,1)
    drag = 50
    
    if gaze.is_blinking():
        text = "Blinking"

    if gaze.is_top():
        text = "Looking Center"

    elif gaze.is_left():
        text = "Looking Left"

    elif gaze.is_center():
        text = "Looking Top"

    elif gaze.is_right():
        text = "Looking Right"

    elif gaze.is_down():
        text = "Looking Down"


    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Gaze Track", frame)

    if(text != text_old):
        print(text)
        sleep(1)
        if(text == "Looking Top" ):
            print("FORWARD")
            
        elif(text == "Looking Right" ):
            print("RIGHT")
            
        elif(text == "Looking Left" ):
            print("LEFT")
            
        elif(text == "Looking Down" ):
            print("BACK")
            
        elif (text == "Blinking"):
            print("Blinking")
            
            

    text_old = text

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
print("Project End")






