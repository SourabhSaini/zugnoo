import fonts
from rgbmatrix import graphics


class Text:
    def __init__(self, canvas):
        self.canvas = canvas

    def display(self, position, text, font, color):
        x, y = position
        graphics.DrawText(
                self.canvas,
                font,
                x, y,
                color,
                text
                )

    def set_color(self, color):
        pass

    def update(self, text):
        pass

    def clear(self):
        pass

    def set_rotation(self, angle):
        pass

    def wrap_text(self, wrap_flag):
        pass

    def get_bbox(self):
        pass

