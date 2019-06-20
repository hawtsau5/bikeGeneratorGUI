import random
import bimpy

class Windows:
    def __init__(self, ctx_context, fonts_data):
        self.ctx = ctx_context
        self.fonts = fonts_data

        self.data = [float(random.randint(90, 300)) for _ in range(50)]

    def draw_time_elapsed_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(3, 3), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(1360, 218), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("Time Elapsed", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[38]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Time Elapsed")
        bimpy.pop_font()
        
        bimpy.separator()

        bimpy.end()

    def draw_power_levels_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(3, 225), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(450, 540), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("Power Levels", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[38]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Power Level")
        bimpy.pop_font()
        
        bimpy.separator()

        bimpy.end()

    def draw_speed_levels_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(458, 225), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(450, 540), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("Speed Levels", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[38]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Speed Levels")
        bimpy.pop_font()
        
        bimpy.separator()

        # ------------------------------ RPM
        bimpy.plot_lines("", self.data, 0, "", graph_size=bimpy.Vec2(285, 65))
        self.data.append(float(random.randint(90, 300)))
        self.data.pop(0)

        bimpy.same_line(0, 10)
        bimpy.push_font(self.fonts.fonts[36]["ext_bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 1, 0, 1), str(int(self.data[0])))
        bimpy.pop_font()

        bimpy.same_line(380, 0)
        bimpy.push_font(self.fonts.fonts[27]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 1, 1, 1), "RPM")
        bimpy.pop_font()


        # ------------------------------ Speed
        bimpy.separator()

        bimpy.plot_lines("", self.data, 0, "", graph_size=bimpy.Vec2(285, 65))
        self.data.append(float(random.randint(90, 300)))
        self.data.pop(0)

        bimpy.same_line(0, 10)
        bimpy.push_font(self.fonts.fonts[36]["ext_bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 1, 0, 1), str(int(self.data[0])))
        bimpy.pop_font()

        bimpy.same_line(380, 0)
        bimpy.push_font(self.fonts.fonts[27]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 1, 1, 1), "Km/H")
        bimpy.pop_font()

        # ------------------------------ Distance
        bimpy.separator()

        bimpy.plot_lines("", self.data, 0, "", graph_size=bimpy.Vec2(285, 65))
        self.data.append(float(random.randint(90, 300)))
        self.data.pop(0)

        bimpy.same_line(0, 10)
        bimpy.push_font(self.fonts.fonts[36]["ext_bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 1, 0, 1), str(int(self.data[0])))
        bimpy.pop_font()

        bimpy.same_line(380, 0)
        bimpy.push_font(self.fonts.fonts[27]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 1, 1, 1), "Km")
        bimpy.pop_font()

        bimpy.end()

    def draw_user_info_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(913, 225), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(450, 540), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("User Info", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[38]["bold_ital"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "User Info")
        bimpy.pop_font()

        bimpy.separator()

        bimpy.end()