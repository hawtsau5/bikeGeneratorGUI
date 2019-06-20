import datetime
import random
import bimpy

class Windows:
    def __init__(self, ctx_context, fonts_data, data):
        self.data = data
        self.ctx = ctx_context
        self.fonts = fonts_data

    def draw_time_elapsed_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(1016, 3), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(350, 250), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("Time Elapsed", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[24]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Time Elapsed")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.text("")
        bimpy.same_line(40, 0)
        bimpy.text(str(datetime.timedelta(seconds=self.data.exercize_time))[:-4])
        bimpy.pop_font()

        bimpy.end()