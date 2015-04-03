class point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def sub(self,p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z

    def add(self,p):
        self.x += p.x
        self.y += p.y
        self.z += p.z

    def add_ret(self,p):
        return point(self.x+p.x, self.y+p.y, self.z+p.z)

    def mul(self,p):
        self.x *= p
        self.y *= p
        self.z *= p

    def com(self,p):
        if self.x == p.x and self.y == p.y and self.z == p.z:
            return 1
        else:
            return 0

    def project(self, dist):
        self.x = self.x * dist/self.y
        self.z = self.z * dist/self.y
        self.y = dist

    def project_ret(self, dist):
        return point(self.x*dist/self.y, dist, self.z*dist/self.y)
