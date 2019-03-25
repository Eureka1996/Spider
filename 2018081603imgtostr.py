#coding=utf-8

from pytesseract import *
from PIL import Image

image = Image.open("second.jpg")
text = image_to_string(image)
print text

