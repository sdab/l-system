import lsystem
import draw
import logging
import utils

# PARAMETERS
IMG_HEIGHT = 1280
IMG_WIDTH = 1920
IMG_HEIGHT = 200
IMG_WIDTH = 200

def draw_2d_lsystem(axiom, rules, angle, iterations):
    ls = lsystem.LSystem(axiom, rules)
    ls.IterateGrammar(iterations)
    #points = list(ls.GeneratePoints(angle, 10, start_point=[IMG_WIDTH/4, IMG_HEIGHT*0.7, 0]))
    points = list(ls.GeneratePoints(angle, 10))

    points = utils.center_points(points)
    
    # Turn 3D into 2D points
    points2D = []
    warn = False
    for p in points:
        (x, y, z) = p
        if z != 0:
            warn = True
        points2D.append((x,y))
    if warn:
        logging.warning("L-System is not 2D, ignoring 3rd dimension.")

    (width, height, depth) = detect_image_size(points)
    width = max(IMG_WIDTH, width)
    height = max(IMG_HEIGHT, height)
    # Draw it
    draw.draw_points(points2D, (width, height))

def detect_image_size(points):
    bounds = utils.find_boundaries(points)
    return [int(b-a) for (a,b) in bounds]
    
if __name__ == "__main__":
    # Create koch snowflake
    draw_2d_lsystem("F--F--F", {"F": "F+F--F+F"}, 60, 5)
    # Create hilbert curve
    draw_2d_lsystem("A", {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"}, 90, 6)
    # Serpinski arrowhead triangle
    draw_2d_lsystem("F", {"F": "G-F-G", "G": "F+G+F"}, 60, 9)

