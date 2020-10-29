# This is an l-system engine that emulates a 3D Logo turtle.
# That is, it takes an axiom, rules, and iteration count and returns a set of
# 3D points that can be connected to form an image.
# It supports the turtle commands like Forward and turn, but is more performant
# than running the actual turtle module and works in 3D.

# It is inspired by https://github.com/dkandalov/lsystem-js.

import math
import numpy
import quaternion
from collections import deque

# Represents a 3D point that should not be connected to. This is how we implement
# brackets in the l-system: http://www1.biologie.uni-hamburg.de/b-online/e28_3/lsys.html.
DONT_CONNECT = (None, None, None)
X_AXIS = (1, 0, 0)
Y_AXIS = (0, 1, 0)
Z_AXIS = (0, 0, 1)


class LSystem:
    # axiom: str
    # rules: dict from str -> str
    # angle: double in degrees
    # step_length: int
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.current_grammar = axiom
        self.rules = rules

    def IterateGrammar(self, iterations=1):
        def sub(x):
            if x in self.rules:
                return self.rules[x]
            return x
        for i in range(iterations):
            self.current_grammar = "".join([sub(x) for x in self.current_grammar])

    def GeneratePoints(self, angle, step_length, start_point = [0, 0, 0], start_dir = [1, 0, 0]):
        yield start_point[:]

        point = numpy.array(start_point)
        step = numpy.array(start_dir) * step_length

        # Note on quaternions to self:
        # Quaternions are a 4D generalization of complex numbers that can be interpreted
        # as axis+angle and produce rotations in 3D.
        # A quaternion vector is (w, x, y, z) where x,y,z is the axis vector and w is related
        # to the angle: https://stackoverflow.com/a/4023264.
        # The function from_euler_angles takes euler angles (a, b, g) in radians and constructs
        # a quaternion according to https://github.com/moble/quaternion/wiki/Euler-angles-are-horrible#conventions.
        direction = quaternion.from_euler_angles(numpy.array(start_dir) * math.radians(0))
        stack = deque()
        
        for c in self.current_grammar:
            if c == "F" or c == "G":
                # Move forward by taking a "step" in the current direction.
                point = numpy.round(point + quaternion.rotate_vectors(direction, step), 2)
                yield point.tolist()
            if c == ">":
                # Rotate direction by angle along x axis
                rotation = quaternion.from_euler_angles(numpy.array(X_AXIS) * math.radians(angle))
                direction = direction * rotation
            if c == "<":
                # Rotate direction by -angle along x axis
                rotation = quaternion.from_euler_angles(numpy.array(X_AXIS) * -math.radians(angle))
                direction = direction * rotation
            if c == "^":
                # Rotate direction by angle along y axis
                rotation = quaternion.from_euler_angles(numpy.array(Y_AXIS) * -math.radians(angle))
                direction = direction * rotation
            if c == "&":
                # Rotate direction by -angle along y axis
                rotation = quaternion.from_euler_angles(numpy.array(Y_AXIS) * math.radians(angle))
                direction = direction * rotation
            if c == "+":
                # Rotate direction by angle along z axis
                rotation = quaternion.from_euler_angles(numpy.array(Z_AXIS) * math.radians(angle))
                direction = direction * rotation
            if c == "-":
                # Rotate direction by -angle along z axis
                rotation = quaternion.from_euler_angles(numpy.array(Z_AXIS) * -math.radians(angle))
                direction = direction * rotation
            if c == '[':
                stack.append((point, direction))
                print("pushing to stack", point, direction)
            if c == ']':
                (point, direction) = stack.pop()
                yield DONT_CONNECT
                yield(point.tolist())
        


    
