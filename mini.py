import cv2 
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
from gtts import gTTS
#import face_recog
# from gpiozero import Button
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
camera.brightness = 55


rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image=cv2.flip(image,-1)
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    #camera.stop_preview()
    #camera.close()

    if key == ord("s"):
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        dilate = cv2.dilate(gray,(3,3),iterations=1)
        adaptive_thresh = cv2.adaptiveThreshold(dilate,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,5)
        text = pytesseract.image_to_string(adaptive_thresh)
        print(text)
        tts = gTTS(text)
        tts.save('hello.mp3')
        cv2.imshow("Frame2",adaptive_thresh)
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()





# button1 = Button(2)
# button2 = Button(17)

# if Button(2):
#     ocr()
# elif Button(17):
#     face_recog.recognize()
# try:
#     while True:
#         button_state = GPIO.input(27)
#         button_state1 = GPIO.input(17)

#         if button_state == False:
#             print("Performing OCR")
#             ocr()
#         if button_state1 == False:
#             print("Performing FR")
#             face_recog.recognize()

# except:
#     GPIO.cleanup()