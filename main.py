import lsystem
import draw
import logging
import utils

# PARAMETERS
# Min image dimensions, draw will  detect larger image size.
IMG_HEIGHT = 200
IMG_WIDTH = 200

def draw_2d_lsystem(axiom, rules, angle, iterations):
    ls = lsystem.LSystem(axiom, rules)
    ls.IterateGrammar(iterations)
    points = list(ls.GeneratePoints(angle, 10))
    points = utils.center_points(points)
    points2D = utils.from_3d_to_2d(points)

    (width, height, depth) = utils.detect_image_size(points)
    width = max(IMG_WIDTH, width)
    height = max(IMG_HEIGHT, height)
    # Draw it
    draw.show_points(points2D, (width, height))

def gif_2d_lsystem(axiom, rules, angle, iterations):
    ls = lsystem.LSystem(axiom, rules)
    all_points = []
    # We need to get every iteration separately as well
    # as the largest one before we scale the earlier
    # iterations.
    for i in range(iterations):
        ls.IterateGrammar()
        points = list(ls.GeneratePoints(angle, 10))
        all_points.append(points)

    # Grab largest image size to scale the rest.
    max_dims = utils.detect_image_size(all_points[-1])

    images = []
    for points in all_points:
        points = utils.scale_points(points, max_dims)
        points = utils.center_points(points)
        points2D = utils.from_3d_to_2d(points)

        (width, height, depth) = max_dims
        width = max(IMG_WIDTH, width)
        height = max(IMG_HEIGHT, height)

        im = draw.draw_points(points2D, (width, height))
        images.append(im)
    # TODO: don't hardcode path
    draw.write_gif(images, "/tmp/fractal.gif")

if __name__ == "__main__":
    # Create koch snowflake
    #draw_2d_lsystem("F--F--F", {"F": "F+F--F+F"}, 60, 5)
    #gif_2d_lsystem("F--F--F", {"F": "F+F--F+F"}, 60, 5)
    # Create hilbert curve
    #draw_2d_lsystem("A", {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"}, 90, 6)
    #gif_2d_lsystem("A", {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"}, 90, 6)
    # Serpinski arrowhead triangle
    #draw_2d_lsystem("F", {"F": "G-F-G", "G": "F+G+F"}, 60, 9)
    # TODO: seems broken, need to debug
    gif_2d_lsystem("F", {"F": "G-F-G", "G": "F+G+F"}, 60, 9)

