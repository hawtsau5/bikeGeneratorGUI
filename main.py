from data_handler.calculation import *
from data_handler.datas import *
from data_handler.sensors import *

sensor = Sensor(21)
# Data Parameters are --> NAME, AGE, WEIGHT, (TRUE FOR FEMALE, FALSE FOR MALE)
data = Data("Wowotek", 22, 90, False)
# Calculator Parameters Are --> DATA CLASS, SENSOR CLASS, WHEEL_CIRCUMFERENCE
calculator = Calculator(data, sensor, 20)

test_time = time.time()
while True:
    calculator.calculate()
    data.pretty_print()
    
    time.sleep(.01)