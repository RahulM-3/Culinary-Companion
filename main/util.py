import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def get_text(img):
    img_array = np.array(img)
    text = pytesseract.image_to_string(img).replace("\n", "")
    for i in range(len(text)-1):
        if(text[i] == "," and text[i+1] != " "):
            return text[:i+1]+" "+text[i+1:]

def get_live_camera_input():
    pass

get_live_camera_input()

import gtts

def generate_speech(text):
    t1 = gtts.gTTS(text)
    t1.save("main/temp_audio/direction.mp3")

