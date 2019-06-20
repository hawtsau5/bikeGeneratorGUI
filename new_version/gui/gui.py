import time, random
import bimpy

from font import Fonts
from window import Windows

ctx = bimpy.Context()
ctx.init(1366, 768, "Test")

style = bimpy.GuiStyle()

style.set_color(bimpy.Colors(2), bimpy.Vec4(0.0, 0.0, 0.26, 1))  # Change Window BG Color

bimpy.set_style(style)
fonts = Fonts()
fonts.load_all_fonts()

windows = Windows(ctx, fonts)


while not ctx.should_close():
    ctx.new_frame()

    windows.draw_time_elapsed_window()
    windows.draw_power_levels_window()
    windows.draw_speed_levels_window()
    windows.draw_user_info_window()

    ctx.render()

    time.sleep(.10)