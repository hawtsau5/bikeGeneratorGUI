import time, random

class Calculator:
    def __init__(self, datas, gpio_controller, circle_circumference):
        self.data = datas
        self.circle_circumference = circle_circumference
        self.gpio_controller = gpio_controller

        self.stop_calculating_tracked = False
        self.stop_calculating_time = 0
        self.stop_calculating_elapsed = 0

    def calculate_speed(self):
        if self.gpio_controller.update_elapsed != 0:
            self.data.rpm = 1/self.gpio_controller.update_elapsed * 60
            self.data.speed[0] = (self.circle_circumference/100000) * 3600
            self.data.speed[1] = (self.circle_circumference/100000) / self.gpio_controller.update_elapsed
            self.data.distance = (self.circle_circumference/100000) * self.gpio_controller.tick

    def calculate(self):
        if not self.data.is_exercising:
            if self.stop_calculating_tracked == False:
                self.stop_calculating_time = time.time()
                self.stop_calculating_tracked = True
            else:
                self.stop_calculating_elapsed = time.time() - self.stop_calculating_time
            return

        self.data.heart_rate = 60
        self.calculate_speed()

        if self.stop_calculating_tracked == True:
            self.stop_calculating_tracked = False
            self.data.exercize_start_time -= self.stop_calculating_tracked - self.stop_calculating_elapsed

        self.data.exercize_time = (time.time() - self.data.exercize_start_time)
        
        age_ratio       = self.data.age * (0.2017 if not self.data.gender else 0.074)
        weight_ratio    = self.data.weight * (0.1988 if not self.data.gender else 0.1263)
        bpm_ratio       = self.data.heart_rate * (0.6309 if not self.data.gender else 0.4472)
        duration_ratio  = self.data.exercize_time / (60 * 4.184)

        self.data.calories_burned = (age_ratio + weight_ratio + bpm_ratio - 55.0969) * duration_ratio