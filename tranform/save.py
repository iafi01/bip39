from PIL import Image, ImageDraw

width, height = 440, 480

boxwidth = width / 11
boxheight = height / 12
img = Image.new('RGB', (width, height), color = 'white')
draw = ImageDraw.Draw(img)

def save(arr):
    for i in range(12):
        for j in range(11):
            x1, y1 = j * boxwidth, i * boxwidth
            x2, y2 = x1 + boxheight, y1 + boxheight
            
            if arr[i][j] == "0":
                draw.rectangle((x1, y1, x2, y2), fill = 'white')
            else:
                draw.rectangle((x1, y1, x2, y2), fill = 'black')

    img.save('scacchiera.png')
    return
