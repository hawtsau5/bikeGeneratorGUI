# from data_handler.calculation import *
# from data_handler.datas import *
# from data_handler.sensors import *

# sensor = Sensor(21)
# data = Data("Wowotek", 22, 90, False)
# calculator = Calculator(data, sensor, 20)

# test_time = time.time()
# while True:
#     calculator.calculate()
#     sensor.callback_function(21)
#     data.pretty_print()
    
#     time.sleep(1)

from data_handler.sensors import *
from data_handler.datas import *
from data_handler.calculation import *
from gui.gui import *

sensor = Sensor(21)
data = Data("Wowotek", 22, 90, False)
calculator = Calculator(data, sensor, 240)
gui = GUI(data)

while True:
    calculator.calculate()
    sensor.callback_function()
    
    gui.draw_window()
    time.sleep(0.012)