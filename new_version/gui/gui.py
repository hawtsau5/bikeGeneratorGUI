import time, random
import bimpy

from data_handler.datas import Data
from gui.font import Fonts
from gui.main_window import MainWindows
from gui.user_input_window import UserInputWindow

class GUI:
    def __init__(self):
        self.data = None

        self.ctx = bimpy.Context()
        self.ctx.init(1015, 636, "Test")

        style = bimpy.GuiStyle()
        style.set_color(bimpy.Colors(2), bimpy.Vec4(0.0, 0.0, 0.26, 1))  # Change Window BG Color

        bimpy.set_style(style)

        self.fonts = Fonts()
        self.fonts.load_all_fonts()

        self.mainWindows = MainWindows(self.fonts, self.data)
        self.userInputWindow = UserInputWindow(self.fonts)

    def draw_window(self):
        if not self.ctx.should_close():
            self.ctx.new_frame()

            if self.data == None:
                self.userInputWindow.draw_window()
            else:
                self.mainWindows.draw_window()

            self.ctx.render()
        else:
            exit()

    def get_data(self):
        return self.data