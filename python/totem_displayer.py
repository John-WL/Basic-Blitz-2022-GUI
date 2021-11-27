import tkinter
from tk_totem_square_data import TkTotemSquareData


class TotemDisplayer:
    def __init__(self):
        self.canvas_dimensions = (700, 700)
        self.tk = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.tk, bg="white", height=self.canvas_dimensions[0], width=self.canvas_dimensions[1])
        self.tk_totem_data = TkTotemSquareData(20, self.canvas_dimensions[0])

    def display(self, totem_answers):
        self.tk_totem_data.clear_rectangles_in_canvas(self.canvas)
        self.tk_totem_data.create_rectangles_in_canvas(self.canvas, totem_answers)
        self.canvas.pack()
        self.tk.update()
