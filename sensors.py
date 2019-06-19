import RPi.GPIO as GPIO

class Sensor:
    tick = 0

    def __init__(self, input_pin):
        self.input_pin = input_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.IN)
        GPIO.setwarnings(False)
        GPIO.add_event_detect(input_pin, GPIO.FALLING, callback=self.callback_function, bouncetime=20)

    def callback_function(self, channel):
        self.tick += 1