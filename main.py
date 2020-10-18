import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import collections
import sys


def show(img):
    plt.imshow(img, cmap="gray")
    plt.show()


def convert_to_monochrome(image, save=''):
    pixels = image.load()
    for i in range(image.size[0]):  # for every pixel:
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            if r > 140 and g > 140 and b > 140:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)

    if save:
        image.save(save)

    return image


filename = sys.argv[1]
new_filename = sys.argv[2]
convert_to_monochrome(Image.open(f'images/{filename}.jpeg'), save=f'images/{new_filename}.jpeg')

strings = pytesseract.image_to_string(f'images/{new_filename}.jpeg').split()
counter = collections.Counter(strings)
print(counter)
