import time, datetime
import random
import bimpy
import textwrap

class MainWindows:
    def __init__(self, fonts_data, data):
        self.data = data
        self.fonts = fonts_data

        self.pause_button_state = 1         # 1 Pause Button Enabled, 0 Resume Button, -1 Pause Button Disabled
        self.stop_button_enabled = True

        self.rpm_datas       = [0 for _ in range(100)]
        self.heart_rate_data = [0 for _ in range(120)]
        self.power_datas     = [0 for _ in range(100)]

        self.heart_rate_start_monitor = time.time()
        self.rpm_start_monitor = time.time()
        self.power_start_monitor = time.time()

    def draw_window(self):
        self.__buttons_window()

        self.__name_window()
        self.__gender_window()
        self.__age_window()

        self.__separator_name_window()

        self.__time_window()
        self.__distance_window()
        self.__calories_burtn_window()
        self.__speed_window()
        self.__heart_rate_window()

        self.__separator_power_window()

        self.__voltage_window()
        self.__current_window()
        self.__power_window()
        self.__rpm_window()

    def __buttons_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 635), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(1005, 128), bimpy.Condition.Once)

        bimpy.begin("Exercise Control", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Controls")
        bimpy.separator()
        bimpy.pop_font()
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text("")
        bimpy.same_line(0, 150)

        if self.pause_button_state == 1:
            bimpy.push_style_color(bimpy.Colors(0), bimpy.Vec4(0, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(21), bimpy.Vec4(0.8, 0.8, 0, 1))
            bimpy.push_style_color(bimpy.Colors(22), bimpy.Vec4(1, 1, 0, 1))
            bimpy.push_style_color(bimpy.Colors(23), bimpy.Vec4(0.5, 0.5, 0, 1))
            pause_button_text = "Pause Exercise"
        elif self.pause_button_state == 0:
            bimpy.push_style_color(bimpy.Colors(0), bimpy.Vec4(0, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(21), bimpy.Vec4(0.0, 0.8, 0.0, 1))
            bimpy.push_style_color(bimpy.Colors(22), bimpy.Vec4(0.0, 1, 0.0, 1))
            bimpy.push_style_color(bimpy.Colors(23), bimpy.Vec4(0.0, 0.5, 0.0, 1))
            pause_button_text = "Resume Exercise"
        elif self.pause_button_state == -1:
            bimpy.push_style_color(bimpy.Colors(0), bimpy.Vec4(0, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(21), bimpy.Vec4(0.4, 0.4, 0.4, 1))
            bimpy.push_style_color(bimpy.Colors(22), bimpy.Vec4(0.4, 0.4, 0.4, 1))
            bimpy.push_style_color(bimpy.Colors(23), bimpy.Vec4(0.4, 0.4, 0.4, 1))
            pause_button_text = "------ -------"

        if bimpy.button(pause_button_text, bimpy.Vec2(250, 75)):
            if self.pause_button_state == 1:
                self.pause_button_state = 0
                self.data.is_exercising = False
            elif self.pause_button_state == 0:
                self.pause_button_state = 1
                self.data.is_exercising = True

        bimpy.pop_style_color()
        bimpy.pop_style_color()
        bimpy.pop_style_color()
        bimpy.pop_style_color()

        bimpy.same_line(450, 150)

        if self.stop_button_enabled:
            bimpy.push_style_color(bimpy.Colors(0) , bimpy.Vec4(0, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(21), bimpy.Vec4(0.8, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(22), bimpy.Vec4(1, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(23), bimpy.Vec4(0.5, 0, 0, 1))
        else:
            bimpy.push_style_color(bimpy.Colors(0) , bimpy.Vec4(0, 0, 0, 1))
            bimpy.push_style_color(bimpy.Colors(21), bimpy.Vec4(0.4, 0.4, 0.4, 1))
            bimpy.push_style_color(bimpy.Colors(22), bimpy.Vec4(0.4, 0.4, 0.4, 1))
            bimpy.push_style_color(bimpy.Colors(23), bimpy.Vec4(0.4, 0.4, 0.4, 1))
            self.pause_button_state = -1

        if bimpy.button("Stop Exercise", bimpy.Vec2(250, 75)):
            self.data.is_exercising = False
            self.stop_button_enabled = False

        bimpy.pop_style_color()
        bimpy.pop_style_color()
        bimpy.pop_style_color()
        bimpy.pop_style_color()

        bimpy.pop_font()

        bimpy.end()

    def __name_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 5), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(720, 80), bimpy.Condition.Once)

        bimpy.begin("Name", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Name")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[16]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(38, 0)
        bimpy.text(self.data.name[:50])
        bimpy.pop_font()

        bimpy.end()

    def __gender_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(729, 5), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(166, 80), bimpy.Condition.Once)

        bimpy.begin("Gender", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Gender")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[16]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(38, 0)
        bimpy.text("Female" if self.data.gender else "Male")
        bimpy.pop_font()

        bimpy.end()

    def __age_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(900, 5), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(110, 80), bimpy.Condition.Once)

        bimpy.begin("Age", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Age")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[16]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(38, 0)
        bimpy.text(str(self.data.age))
        bimpy.pop_font()

        bimpy.end()

    def __separator_name_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 90), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(1005, 38), bimpy.Condition.Once)

        bimpy.begin("Separator Name", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        bimpy.separator()
        bimpy.text("")
        bimpy.separator()
        bimpy.end()

    def __voltage_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 278 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)

        bimpy.begin("Voltage", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Voltage")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        if self.data.voltage >= 0:
            bimpy.text("{:.2f}".format(self.data.voltage).rjust(6, "0"))
        else:
            bimpy.text("-" + "{:.2f}".format(self.data.voltage).rjust(5, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(220, 0)
        bimpy.text("Volt")
        bimpy.pop_font()

        bimpy.end()
    
    def __current_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 393 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)

        bimpy.begin("Current", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Current")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        bimpy.text("{:.2f}".format(self.data.voltage).rjust(6, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(215, 0)
        bimpy.text("Amp")
        bimpy.pop_font()

        bimpy.end()

    def __power_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(355, 278 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 225), bimpy.Condition.Once)

        bimpy.begin("Power", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Power")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        bimpy.text("{:.2f}".format(self.data.power).rjust(6, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(212, 0)
        bimpy.text("Watts")
        bimpy.pop_font()
        
        self.power_datas.append(self.data.power)
        self.power_datas.pop(0)

        self.power_datas.reverse()
        bimpy.plot_lines("", self.power_datas, graph_size=bimpy.Vec2(329, 112), scale_min=-1.0, scale_max=500.0)
        self.power_datas.reverse()

        bimpy.end()

    def __rpm_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(705, 278 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(305, 225), bimpy.Condition.Once)

        bimpy.begin("RPM", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "RPM")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        bimpy.text(str(int(self.data.rpm)).rjust(4, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(175, 0)
        bimpy.text("RPM")
        bimpy.pop_font()

        self.rpm_datas.append(self.data.rpm)
        self.rpm_datas.pop(0)

        self.rpm_datas.reverse()
        bimpy.plot_lines("", self.rpm_datas, graph_size=bimpy.Vec2(288, 112))
        self.rpm_datas.reverse()
        bimpy.end()

    def __separator_power_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 235 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(1005, 38), bimpy.Condition.Once)

        bimpy.begin("Separator Power", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        bimpy.separator()
        bimpy.text("")
        bimpy.separator()
        bimpy.end()

    def __time_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 5 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)

        bimpy.begin("Time Elapsed", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Time Elapsed")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(38, 0)
        bimpy.text(str(datetime.timedelta(seconds=self.data.exercize_time))[:-4])
        bimpy.pop_font()

        bimpy.end()

    def __distance_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 120 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)

        bimpy.begin("Distance", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Distance Traveled")
        bimpy.pop_font()
        bimpy.separator()

        if self.data.distance <= 1.1 :
            distance_formatted_data = str(int(self.data.distance * 1000))
            distance_formatted_data = distance_formatted_data.rjust(4, "0")
            scalar = "m"
        else:
            distance_formatted_data = "{:.2f}".format(self.data.distance)
            distance_formatted_data = distance_formatted_data.rjust(6, "0")
            scalar = "Km"

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(38, -1)
        bimpy.text(distance_formatted_data)
        bimpy.same_line(245, 0)
        bimpy.text(scalar)
        bimpy.pop_font()

        bimpy.end()

    def __calories_burtn_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(355, 5 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)

        bimpy.begin("Calories Burnt", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Calories Burnt")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        if self.data.calories_burned >= 0:
            bimpy.text("{:.2f}".format(self.data.calories_burned).rjust(7, "0"))
        else:
            bimpy.text("0.00".rjust(7, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(250, 0)
        bimpy.text("cal")
        bimpy.pop_font()

        bimpy.end()

    def __speed_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(355, 120 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)

        bimpy.begin("Speed", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Speed")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        bimpy.text(str(int(self.data.speed[0])).rjust(4, " "))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(200, 0)
        bimpy.text("Km/H")
        bimpy.pop_font()

        bimpy.end()

    def __heart_rate_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(705, 5 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(305, 225), bimpy.Condition.Once)

        bimpy.begin("Heart Rate", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        
        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Heart Rate")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.text("")

        bimpy.same_line(30, -1)

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text(str(int(self.data.heart_rate)).rjust(3, "0"))
        bimpy.pop_font()

        bimpy.same_line(140, 20)

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("BPM")
        bimpy.pop_font()
        
        if (time.time() - self.heart_rate_start_monitor) >= (self.data.heart_rate / 60):
            self.heart_rate_data.append(-0.7)
            self.heart_rate_data.append(1)
            self.heart_rate_start_monitor = time.time()
            self.heart_rate_data.pop(0)
        else:
            self.heart_rate_data.append(0)

        self.heart_rate_data.pop(0)

        self.heart_rate_data.reverse()
        bimpy.plot_lines("", self.heart_rate_data, graph_size=bimpy.Vec2(288, 112), scale_min=-1.0, scale_max=1.3)
        self.heart_rate_data.reverse()

        bimpy.end()