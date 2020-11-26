import lsystem

# Returns the boundaries of the given points
# as min,max tuples for each dimension.
def find_boundaries(points):
    min_x = min([x for (x, y, z) in points])
    min_y = min([y for (x, y, z) in points])
    min_z = min([z for (x, y, z) in points])

    max_x = max([x for (x, y, z) in points])
    max_y = max([y for (x, y, z) in points])
    max_z = max([z for (x, y, z) in points])

    return ((min_x, max_x), (min_y, max_y), (min_z, max_z))

# TODO: test
# Returns the image size based on the given points.
def detect_image_size(points):
    bounds = find_boundaries(points)
    return [int(b-a) for (a,b) in bounds]
    
# Translates the points so that the image is centered.
def center_points(points):
    init_bounds = find_boundaries(points)
    offsets = [0-a for (a, b) in init_bounds]

    new_points = []
    for p in points:
        if p == lsystem.DONT_CONNECT:
            new_points.append(p)
            continue
        new_points.append(list(a+b for a,b in zip(p, offsets)))
    return new_points

# TODO: test
# Returns a set of points such that the given points are scaled to have the
# desired dimensions.
def scale_points(points, dims):
    (width, height, depth) = dims
    # current height and width
    (w, h, d) = detect_image_size(points)
    scaleX = width/w if w else 0
    scaleY = height/h if h else 0
    scaleZ = depth/d if d else 0

    p = []
    for (x,y,z) in points:
        p.append((x*scaleX, y*scaleY, z*scaleZ))
    return p

# TODO: test
# Returns a set of 2D points from the given 3D points. The given 3D points
# are expected to have z=0 for every point.
def from_3d_to_2d(points):
    points2D = []
    warn = False
    for p in points:
        (x, y, z) = p
        if z != 0:
            warn = True
        points2D.append((x,y))
    if warn:
        logging.warning("L-System is not 2D, ignoring 3rd dimension.")
    return points2D
