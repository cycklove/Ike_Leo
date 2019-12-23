import pytesseract as pt

from PIL import Image

im = Image.open('C:\\Users\Ike_Leo\Desktop\cp3.jpg')

text = pt.image_to_string(im)
# print(text)