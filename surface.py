from point import point

class surface:
    def __init__(self, kind='tri', a=point(),b=point(),c=point(),d=point(),
                 input_b=0, input_g=255, input_r=0):
        self.surface_type = kind
        self.b = input_b 
        self.g = input_g
        self.r = input_r
        if kind=='rect':
            self.createRect(a,b,c,d)
        elif kind=='tri':
            self.createTri(a,b,c)

    def createRect(self, x1=point(), x2=point(), x3=point(), x4=point()):
        self.p1=x1
        self.p2=x2
        self.p3=x3
        self.p4=x4

    def createTri(self, x1=point(), x2=point(), x3=point()):
        self.p1=x1
        self.p2=x2
        self.p3=x3

    def liesontri(self, pt):
        if pt.x < 10 and pt.x > -10 and pt.z > -10 and pt.z < 10:
            return 1
        else:
            return 0
