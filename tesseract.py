import cv2 
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera


# img = cv2.imread('shell.png')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# text = pytesseract.image_to_string(img)
# print(text)
# cv2.imshow('Result',img)
# cv2.waitKey(0)


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15
camera.brightness = 55

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image=cv2.flip(image,-1)
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("s"):
        text = pytesseract.image_to_string(image)
        print(text)
        cv2.imshow("Frame",image)
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()