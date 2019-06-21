from data_handler.sensors import *
from data_handler.datas import *
from data_handler.calculation import *
from gui.gui import *

sensor = Sensor(21)
gui = GUI()
data = gui.get_data()

calculator = Calculator(data, sensor, 240)

while True:
    calculator.calculate()
    sensor.callback_function()
    
    gui.draw_window()
    time.sleep(0.048)