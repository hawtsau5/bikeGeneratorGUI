import datetime
import random
import bimpy
import textwrap

class MainWindows:
    def __init__(self, fonts_data, data):
        self.data = data
        self.fonts = fonts_data

    def draw_window(self):
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

    def __name_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 5), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(720, 80), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

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
        bimpy.set_next_window_focus()

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
        bimpy.set_next_window_focus()

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
        bimpy.set_next_window_focus()

        bimpy.begin("Separator Name", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        bimpy.separator()
        bimpy.text("")
        bimpy.separator()
        bimpy.end()

    def __voltage_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 278 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("Voltage", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Voltage")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        bimpy.text("{:.2f}".format(self.data.voltage).rjust(6, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(220, 0)
        bimpy.text("Volt")
        bimpy.pop_font()

        bimpy.end()
    
    def __current_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 393 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

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
        bimpy.set_next_window_focus()

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
        bimpy.same_line(215, 0)
        bimpy.text("Amp")
        bimpy.pop_font()

        bimpy.plot_lines("", [float(random.randint(50, 120)) for _ in range (10)], graph_size=bimpy.Vec2(329, 112), scale_min=-1.0, scale_max=500.0)

        bimpy.end()

    def __rpm_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(705, 278 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(305, 225), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

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

        bimpy.plot_lines("", [float(random.randint(50, 120)) for _ in range (10)], graph_size=bimpy.Vec2(288, 112), scale_min=-1.0, scale_max=500.0)

        bimpy.end()

    def __separator_power_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 235 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(1005, 38), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

        bimpy.begin("Separator Power", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))
        bimpy.separator()
        bimpy.text("")
        bimpy.separator()
        bimpy.end()

    def __time_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(5, 5 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

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
        bimpy.set_next_window_focus()

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
        bimpy.set_next_window_focus()

        bimpy.begin("Calories Burnt", flags=bimpy.WindowFlags(4) | bimpy.WindowFlags(1) | bimpy.WindowFlags(2))

        bimpy.push_font(self.fonts.fonts[16]["cond"])
        bimpy.text_colored(bimpy.Vec4(1, 0, 0, 1), "Calories Burnt")
        bimpy.pop_font()
        bimpy.separator()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.text("")
        bimpy.same_line(25, 0)
        bimpy.text("{:.2f}".format(self.data.calories_burned).rjust(7, "0"))
        bimpy.pop_font()

        bimpy.push_font(self.fonts.fonts[44]["ext_bold_ital"])
        bimpy.same_line(250, 0)
        bimpy.text("cal")
        bimpy.pop_font()

        bimpy.end()

    def __speed_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(355, 120 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(345, 110), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

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
        bimpy.text("KmH")
        bimpy.pop_font()

        bimpy.end()

    def __heart_rate_window(self):
        bimpy.set_next_window_pos(bimpy.Vec2(705, 5 + 128), bimpy.Condition.Once)
        bimpy.set_next_window_size(bimpy.Vec2(305, 225), bimpy.Condition.Once)
        bimpy.set_next_window_focus()

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
        
        bimpy.plot_lines("", [float(random.randint(50, 120)) for _ in range (10)], graph_size=bimpy.Vec2(288, 112), scale_min=-1.0, scale_max=150.0)

        bimpy.end()