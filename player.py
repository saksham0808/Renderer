from math import *
from point import point

class player:
    def __init__(self, input_dir=0):
        # Coordinates of player
        self.position = point()
        # Angle of view from Y axis in horizontal plane in degrees
        self.direction = input_dir
	# Horizontal field of view in degrees
	self.xFOV = 90 
	# Vertical field of view in degrees
	self.xFOV = 90
        # Picture plane distance
	self.ppdist = 350

    # To move player
    # r can be positive or negative
    # Theta is angle with z axis, take it from 0 to pi/2
    # Phi is angle of projection with x, take it from 0 to pi/2
    def move(self, r, theta, phi):
        theta   = theta*3.1415/180
        phi     = phi*3.1415*180
        self.position.x += (r*sin(theta)*cos(phi))
        self.position.y += (r*sin(theta)*sin(phi))
        self.position.z += (r*cos(theta))

    def rotate(self, angle):
        self.direction += angle

    def findfinal(self, pt):
        return pt
