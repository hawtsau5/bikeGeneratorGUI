import time
# import RPi.GPIO as GPIO

class Sensor:
    tick = 0
    update_start = time.time()
    update_elapsed = 0

    def __init__(self, input_pin):
        self.input_pin = input_pin

        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(21, GPIO.IN)
        # GPIO.setwarnings(False)
        # GPIO.add_event_detect(input_pin, GPIO.FALLING, callback=self.callback_function, bouncetime=20)

    def callback_function(self, channel=0):
        self.tick += 1
        self.update_elapsed = time.time() - self.update_start
        self.update_start = time.time()