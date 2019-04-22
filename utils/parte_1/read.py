#lendo as imagens com a biblioteca pillow do Python

from PIL import Image

img = Image.open('images/image.jpg')
img.show()