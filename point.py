class point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add_ret(self,p):
        return point(self.x+p.x, self.y+p.y, self.z+p.z)

    def project(self, dist):
        self.x = self.x * dist/self.y
        self.z = self.z * dist/self.y
        self.y = dist


    def mod(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


def add(p1,p2):
    return point(p1.x+p2.x, p1.y+p2.y, p1.z+p2.z)

def sub(p1,p2):
    return point(p1.x-p2.x, p1.y-p2.y, p1.z-p2.z)

def mul(p1,a):
    return point(p1.x*a*1.0, p1.y*a*1.0, p1.z*a*1.0)

def div(p1,a):
    return point(p1.x/a, p1.y/a, p1.z/a)

def com(p1,p2):
    if p1.x==p2.x and p1.y==p2.y and p1.z==p2.z:
        return 1
    else:
        return 0

def dot(p1, p2):
    return p1.x*p2.x + p1.y*p2.y + p1.z*p2.z

def cross(p1, p2):
    return point(p1.y*p2.z-p1.z*p2.y, p1.z*p2.x-p2.z*p1.x, p1.x*p2.y-p1.y*p2.x)

def project(p1, dist):
    return point(p1.x*dist/p1.y, dist, p1*dist/p1.y)
