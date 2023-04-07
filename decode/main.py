from PIL import Image
import decode

arr = []
temp = ""

img = Image.open('scacchiera.png')
for i in range(12):
    temp = ""
    for j in range(11):
        pixel_value = img.getpixel((j * 40, i * 40))
        if (pixel_value == (255, 255, 255)):
            temp += "0"
        elif(pixel_value == (0, 0, 0)):
            temp += "1"
    arr.append(temp)
decode.decode(arr)
