import pytesseract
from PIL import Image
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'


def original(photo):
    # img=Image.open(photo)
    myText = image_to_string(Image.open(photo))
    return myText


def convertL(photo):
    img = Image.open(photo)
    rm = img.convert('L')
    rm.save('newL.png')
    myText1 = image_to_string(Image.open('newL.png'))
    return myText1


def convert1(photo):
    img2 = Image.open(photo)
    rm = img2.convert('1')
    rm.save('new1.png')
    myText2 = image_to_string(Image.open('new1.png'))
    return myText2


photo = 'samples\\asos.png'
dataO = original(photo)
print(dataO)
dataL = convertL(photo)
print(dataL)
data1 = convert1(photo)
print(data1)

# print(myText)
# img=Image.open('761545-outlet-2.jpg')
##thresh=200
##fn = lambda x : 255 if x > thresh else 0
##r = img.convert('L').point(fn, mode='1')
##r.save('foo.png')
##myText = image_to_string(Image.open('foo.png'))
##print(myText)
##img2=Image.open('foo.png')
# rm=img.convert('1')
# rm.save('new.png')
# myText2 = image_to_string(Image.open('new.png'))
# print(myText2)
