from PIL import Image,ImageDraw
import random

WIDTH = 500
HEIGHT = 500

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0,WIDTH):
    for y in range(0,HEIGHT):
        colour = random.randint(0,256)
        draw.point([x, y], (colour, colour, colour))
im.save(f'output.png', 'PNG')
