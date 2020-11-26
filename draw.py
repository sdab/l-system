# This package takes a set of points and draws them in 2D.
# It treats the points sequentially and connects them with lines
# to simulate the Logo Turtle system.

from PIL import Image, ImageDraw
import imageio

# Forest Green RGP tuple
COLOR = (0, 139, 139)
#WIDTH = 1
# TODO: autodetect based on image size
WIDTH = 10

def show_points(points, img_dimension, color=COLOR, width=WIDTH):
    im = draw_points(points, img_dimension, color, width)
    im.show()
    
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

    return im

def write_gif(images, path):
    imageio.mimsave(path, images, duration=0.5)
    
