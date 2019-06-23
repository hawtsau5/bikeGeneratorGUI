import time, random
import bimpy

from data_handler.datas import Data
from gui.font import Fonts
from gui.main_window import MainWindows

class GUI:
    def __init__(self, data):
        self.data = data

        self.ctx = bimpy.Context()
        self.ctx.init(1015, 768, "Test")

        style = bimpy.GuiStyle()
        style.set_color(bimpy.Colors(2), bimpy.Vec4(0.0, 0.0, 0.26, 1))  # Change Window BG Color

        bimpy.set_style(style)

        self.fonts = Fonts()
        self.fonts.load_all_fonts()

        self.mainWindows = MainWindows(self.fonts, self.data)
        self.data.exercize_start_time = time.time()

    def draw_window(self):
        if not self.ctx.should_close():
            self.ctx.new_frame()

            self.mainWindows.draw_window()

            self.ctx.render()
        else:
            exit()