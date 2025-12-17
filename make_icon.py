from PIL import Image

img = Image.open("logo.png")
img.save("icon.ico", sizes=[(256,256)])
