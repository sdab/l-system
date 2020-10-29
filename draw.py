# This package takes a set of points and draws them in 2D.
# It treats the points sequentially and connects them with lines
# to simulate the Logo Turtle system.

from PIL import Image, ImageDraw

# Forest Green RGP tuple
COLOR = (34, 139, 34)
WIDTH = 1

def draw_points(points, img_dimension, color=COLOR, width=WIDTH):
    im= Image.new("RGB", img_dimension, "#FFFFFF")
    draw = ImageDraw.Draw(im)

    prev = None
    for (x, y) in points:
        if x == None or y == None:
            prev = None
            continue
        if prev != None:
            (xx, yy) = prev
            draw.line((xx, yy, x, y), fill=color, width=width)
        prev = (x, y)

    im.show()
