from tkinter import *
from DataStructures import * 
from vectormath import * 

class RenderCore:
    canvas: Canvas = None

    def __init__(self, canvas):
        self.canvas = canvas
    
    def  DrawLine(self, pos1: Vector3, pos2: Vector3, color1: Color, color2: Color = None):
        pass
        #self.canvas.create_line()