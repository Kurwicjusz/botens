from PIL import Image, ImageGrab
import numpy as np
import cv2
from matplotlib import pyplot


def center_image(image):
    width, height = image.size
    #print(width, height)
    left = 1129
    top = 621
    right = left+17
    bottom = top+17
    return ((left, top, right, bottom))

def read_image(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)

def crop_image(image, left, top, right, bottom):
    cropped = image.crop((left, top, right, bottom))
    return cropped

image_path = "tmp.bmp"
image = read_image(image_path)
#image.show()
center = center_image(image)
print(center)
left, top, right, bottom = center
image_cropped = crop_image(image, left, top, right, bottom)
#image_cropped.show()
image_cropped.save(r'cropped.bmp')
image_gray=cv2.imread("cropped.bmp", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image_gray, cv2.COLOR_BGR2GRAY)
ret, threshold1 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
pyplot.imshow(threshold1, 'gray')
#pyplot.show()
print(type(pyplot), type(threshold1))
pyplot.imsave('meme.jpg', threshold1)
image_compare1=cv2.imread("cropped.bmp", cv2.IMREAD_GRAYSCALE)
image_compare2=cv2.imread("meme.jpg", cv2.IMREAD_GRAYSCALE)
image_compare3=cv2.imread("tmp.bmp", cv2.IMREAD_GRAYSCALE)
compare1= cv2.threshold(image_compare1, 150, 255, cv2.THRESH_BINARY)
compare2= cv2.threshold(image_compare2, 150, 255, cv2.THRESH_BINARY)
compare3= cv2.threshold(image_compare3, 150, 255, cv2.THRESH_BINARY)
print(type(compare1), type(compare2))
if (compare1[0]-compare1[0]):
    print('meme1')
if (compare1[1]-compare2[1]).all():
    print('meme')
else:
    print('guwno')

# threshold1.show()
#1129 621 17x17