import tkinter as tk
from data_handler.sensors import *
from data_handler.datas import *
from data_handler.calculation import *
from gui.user_input_window import UserInputApplication
from gui.gui import *

data = Data(name="", age=0, weight=0, gender="")

uia = UserInputApplication(data)
uia.master.title("Please Provide Your Information, so we can hack your computer")
uia.master.maxsize(1366, 636)
uia.mainloop()

if not data.validate(): exit()

sensor      = Sensor(21)
calculator  = Calculator(data, sensor, 240)
gui         = GUI(data)

while True:
    calculator.calculate()
    sensor.callback_function()
    
    gui.draw_window()
    time.sleep(0.006)