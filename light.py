from point import point

class light:
    def __init__(self, x=40,y=20,z=5, b=255,g=255,r=255):
        self.pos = point(x,y,z)
        self.b = b
        self.g = g
        self.r = r
