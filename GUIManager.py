import tkinter as tk
import DataStructures as data
class GUI:
    win = tk.Tk()
    canvas = None
    
    def __init__(self):
        canvas = tk.Canvas(self.win, width = 1000, height=800, bg='black')
        self.canvas = canvas
        canvas.pack()
        color = data.Color(0,1,0)
        canvas.create_line(20, 20, 21, 20, fill=color.GetColor())
        self.initalizeMainWindow()

    def initalizeMainWindow(self):
        self.win.title("Render Engine")
        self.win.geometry("1000x800")
        self.win.mainloop()
    
    def updateMainWindow(self):
         self.win.mainloop()
    
    def GetCanvas(self):
        return self.canvas
    
    def Update(self):
        pass
    

