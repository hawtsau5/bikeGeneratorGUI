import time
import math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)


class LiveData:
    def __init__(self):                
        self.dist_meas = 0.00
        self.km_per_hour = 0
        self.rpm = 0
        self.elapse = 0
        self.sensor = 21
        self.pulse = 0
        self.start_timer = time.time()

        GPIO.add_event_detect(  self.sensor, GPIO.FALLING,
                                callback=self.update_elapsed_time, bouncetime=20)

    def update_elapsed_time(self):
        self.pulse+=1                                # increase pulse by 1 whenever interrupt occurred
        self.elapse = time.time() - self.start_timer      # elapse for every 1 complete rotation made!
        self.start_timer = time.time()               # let current time equals to start_timer

    def calculate_speed(self, r_cm):
        if self.elapse != 0:                          # to avoid DivisionByZero error
            self.rpm = 1/self.elapse * 60
            circ_cm = (2*math.pi)*r_cm          # calculate wheel circumference in CM
            dist_km = circ_cm/100000            # convert cm to km
            km_per_sec = dist_km / self.elapse       # calculate KM/sec
            km_per_hour = km_per_sec * 3600     # calculate KM/h
            self.dist_meas = (dist_km*self.pulse)*1000    # measure distance traverse in meter
            
            return km_per_hour

    def get_rpm(self):
        self.calculate_speed(20) # call this function with wheel radius as parameter
        print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(self.rpm, self.km_per_hour, self.dist_meas, self.pulse))
        return self.rpm