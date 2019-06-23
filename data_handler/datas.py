import time

class Data:
    power = 0
    voltage = 0
    current = 0
    battery = 0

    speed = [
        0,  # KM PER HOUR
        0   # KM PER SEC
    ]
    rpm = 0
    distance = 0
    
    exercize_start_time = time.time()
    exercize_time = 0
    calories_burned = 0
    heart_rate = 0

    def __init__(self, name="", age=0, weight=0, gender=None):
        self.name = name
        self.age = age
        self.gender = gender    # false for male, true for female
        self.weight = weight
        
        self.is_exercising = True

    def validate(self):
        nv = True if self.name != "" else False
        gv = True if self.age != 0 else False
        dv = True if self.gender != None else False
        wv = True if self.weight != 0 else False

        return nv and gv and dv and wv

    def pretty_print(self):
        print("exerTime : {:.2f} calBurnt : {:.2f} bpm : {:.2f} rpm : {:.2f} dist : {:.5f}".format(
            self.exercize_time, self.calories_burned,
            self.heart_rate, self.rpm, self.distance*1000
        ))