from data_handler.calculation import *
from data_handler.datas import *
from data_handler.sensors import *

sensor = Sensor(21)
data = Data("Wowotek", 22, 90, False)
calculator = Calculator(data, sensor, 20)


#------------------------------------------
'''
this is to test the program
so basically it's a unended loop
and looped every second
it simulate sensor detected the rotation magnet sensors every second


'''

test_time = time.time()
while True:
    calculator.calculate()
    sensor.callback_function(21)
    data.pretty_print()
    

    time.sleep(1)