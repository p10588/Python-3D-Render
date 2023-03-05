class Vector3:
    x : float =0
    y : float =0
    z : float =0
    __slot__= (x,y,z)

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


class Color:
    r : float= 0
    g : float= 0
    b : float= 0
    def __init__(self,r: float,g: float,b: float):
        self.r = r
        self.g = g 
        self.b = b

    def GetColor(self):
        color = "#%02x%02x%02x" % (self.r*255, self.g*255, self.b*255) 
        print(color)
        return color
    
    