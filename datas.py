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

    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.gender = gender    # false for male, true for female
        self.weight = weight

    
    def pretty_print(self):
        print("exerTime : {:.2f} calBurnt : {:.2f} bpm : {:.2f} rpm : {:.2f} dist : {:.2f}".format(
            self.exercize_time, self.calories_burned,
            self.heart_rate, self.rpm, self.distance
        ))