import time

class Data:
    timer = time.time()
    elapsed = 0

    power = 0
    voltage = 0
    current = 0
    battery = 0

    rpm = 0
    speed = [
        0,  # KM PER HOUR
        0   # KM PER SEC
    ]
    distance = 0
    elapsed_time = 0

    calories_burned = 0
    heart_beat = 0

    def __init__(self, name, age, circle_circumference):
        self.name = name
        self.age = age
        self.circle_circumference = circle_circumference

    def calculate_elapse(self):
        self.elapse = time.time() - self.timer      # elapse for every 1 complete rotation made!
        self.timer = time.time()  

    def calculate_speed(self, circ_cm):
        if self.elapse != 0:
            self.rpm = 1/self.elapse * 60
            self.speed[0] = (circ_cm/100000) * 3600
            self.speed[1] = (circ_cm/100000) / self.elapse
            self.distance = (circ_cm/100000) * gpio_ticks

    def calculation(self):
        self.start = time.time()
        self.calories_burned = 0
        
        while True:
            a.update()
            heart_rate = 60.0
            self.calculate_speed(self.circle_circumference)
            # print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(rpm,km_per_hour,dist_meas,pulse))
            time.sleep(0.1)
            total_time = time.time() - start
            update_RPM_data(round(rpm,2), round(km_per_hour,2),round(dist_meas,2), round(total_time,2))
            time.sleep(.1)
            
            if g == ('m' or g == 'M'):
                calories_burned = ((0.02017*n)-(0.1988*w)+(0.6309*heart_rate-55.0969))*(total_time/4.184)
                
            if (g == 'f' or g =='F'):
                calories_burned = ((0.074*n)-(0.1263*w)+(0.4472*heart_rate-20.4022))*(total_time/4.184)
                
            time.sleep(.1)