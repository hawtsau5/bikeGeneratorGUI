import time, random
import bimpy

from gui.font import Fonts
from gui.window import Windows


class GUI:
    def __init__(self, data):
        self.data = data

        self.ctx = bimpy.Context()
        self.ctx.init(1366, 768, "Test")

        style = bimpy.GuiStyle()
        style.set_color(bimpy.Colors(2), bimpy.Vec4(0.0, 0.0, 0.26, 1))  # Change Window BG Color

        bimpy.set_style(style)

        self.fonts = Fonts()
        self.fonts.load_all_fonts()

        self.windows = Windows(self.ctx, self.fonts, self.data)

    def draw_window(self):
        if not self.ctx.should_close():
            self.ctx.new_frame()

            self.windows.draw_time_elapsed_window()

            self.ctx.render()
        else:
            exit()