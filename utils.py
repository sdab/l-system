import lsystem

def find_boundaries(points):
    min_x = min([x for (x, y, z) in points])
    min_y = min([y for (x, y, z) in points])
    min_z = min([z for (x, y, z) in points])

    max_x = max([x for (x, y, z) in points])
    max_y = max([y for (x, y, z) in points])
    max_z = max([z for (x, y, z) in points])

    return ((min_x, max_x), (min_y, max_y), (min_z, max_z))

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
