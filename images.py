from PIL import Image, ImageFilter

img = Image.open('rockstar.jpg')
img.thumbnail((400, 400))
img.save('thumnbail.jpg')
img.show()

print(img.size)
