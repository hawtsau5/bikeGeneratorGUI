from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import math
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(21, GPIO.IN)

def calculate_elapse(channel):              # callback function
    global pulse, start_timer, elapse
    pulse+=1                                # increase pulse by 1 whenever interrupt occurred
    elapse = time.time() - start_timer      # elapse for every 1 complete rotation made!
    start_timer = time.time()               # let current time equals to start_timer

def calculate_speed(circ_cm):
    global pulse,elapse,rpm,dist_km,dist_meas,km_per_sec,km_per_hour
    if elapse !=0:                          # to avoid DivisionByZero error
        rpm = 1/elapse * 60          
        dist_km = circ_cm/100000            # convert cm to km
        km_per_sec = dist_km / elapse       # calculate KM/sec
        km_per_hour = km_per_sec * 3600     # calculate KM/h
        dist_meas = dist_km*pulse           # measure distance traversed in kilometer
        return km_per_hour

def init_interrupt():
    GPIO.add_event_detect(sensor, GPIO.FALLING, callback = calculate_elapse, bouncetime = 20)

def start_calculations(n, g, w):          #parameters are age,gender,weight
    init_interrupt()
    start = time.time()
    calories_burned = 0
    print(n,g,w)
    
    while True:
        a.update()
        heart_rate = 60.0
        calculate_speed(20)                 # call this function with wheel radius as parameter
        print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(rpm,km_per_hour,dist_meas,pulse))
        time.sleep(0.1)
        total_time = time.time() - start
        update_RPM_data(round(rpm,2), round(km_per_hour,2),round(dist_meas,2), round(total_time,2))
        time.sleep(.1)
        
        if g == ('m' or g == 'M'):
            calories_burned = ((0.02017*n)-(0.1988*w)+(0.6309*heart_rate-55.0969))*(total_time/4.184)
            
        if (g == 'f' or g =='F'):
            calories_burned = ((0.074*n)-(0.1263*w)+(0.4472*heart_rate-20.4022))*(total_time/4.184)
            
        update_calorie_data(round(calories_burned,2))
        time.sleep(.1)
        

def click():
    name = name_entry.get()
    gender = gender_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    
    age = float(age)
    weight = float(weight)
    
    live_window(name, age)
    start_calculations(age, gender, weight)

def live_window(x,y):          #parameters are name, age
    enter_name.destroy()
    enter_gender.destroy()
    enter_age.destroy()
    enter_weight.destroy()#destroy all whidgets
    enter_button.destroy()                            
    name_entry.destroy()
    gender_entry.destroy()
    age_entry.destroy()
    weight_entry.destroy()

    create_live_whidgets(x,y)
    place_live_whidgets()
    
    
def update_RPM_data(r,s,d,t):             #parameters are rpm, speed, distance, time
    a.rpm_data_label["text"] = r
    a.speed_data_label["text"] = s
    a.distance_data_label["text"] = d
    a.elapsed_data_time["text"] = t
    
def update_calorie_data(c):               #parameter is calories
    a.calorie_data_label["text"] = c

def create_live_whidgets(x,y): 
    a.first_frame         = tk.LabelFrame(a, text='Power Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.power_label         = tk.Label(a.first_frame, text="power :", font=frameFont, bg=frameBG, fg=frameTC) #create power labels
    a.voltage_label       = tk.Label(a.first_frame, text="voltage :", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_label       = tk.Label(a.first_frame, text="current :", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_label       = tk.Label(a.first_frame, text="battery :", font=frameFont, bg=frameBG, fg=frameTC)
    a.power_data_label    = tk.Label(a.first_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC) #create rpm labels
    a.voltage_data_label  = tk.Label(a.first_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_data_label  = tk.Label(a.first_frame, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_data_label  = tk.Label(a.first_frame, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.power_unit_label    = tk.Label(a.first_frame, text="W", font=frameFont, bg=frameBG, fg=frameTC) #create rpm labels
    a.voltage_unit_label  = tk.Label(a.first_frame, text="V", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_unit_label  = tk.Label(a.first_frame, text="A", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_unit_label  = tk.Label(a.first_frame, text="%", font=frameFont, bg=frameBG, fg=frameTC)

    a.second_frame        = tk.LabelFrame(a, text='Speed Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.rpm_label           = tk.Label(a.second_frame, text="RPM :", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_label         = tk.Label(a.second_frame, text="speed :", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_label      = tk.Label(a.second_frame, text="distance :", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_time        = tk.Label(a.second_frame, text="time elapsed :", font=frameFont, bg=frameBG, fg=frameTC)
    a.rpm_data_label      = tk.Label(a.second_frame, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_data_label    = tk.Label(a.second_frame, text="  ", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_data_label = tk.Label(a.second_frame, text=" ", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_data_time   = tk.Label(a.second_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.rpm_unit_label      = tk.Label(a.second_frame, text="rpms", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_unit_label    = tk.Label(a.second_frame, text="kmph", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_unit_label = tk.Label(a.second_frame, text="km", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_unit_time   = tk.Label(a.second_frame, text="s", font=frameFont, bg=frameBG, fg=frameTC)


    a.third_frame         = tk.LabelFrame(a, text='User Info', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.name_label          = tk.Label(a.third_frame, text="name :", font=frameFont, bg=frameBG, fg=frameTC)
    a.age_label           = tk.Label(a.third_frame, text="age :", font=frameFont, bg=frameBG, fg=frameTC)
    a.heart_label         = tk.Label(a.third_frame, text="heart rate :", font=frameFont, bg=frameBG, fg=frameTC)
    a.calorie_label       = tk.Label(a.third_frame, text="calories burned :", font=frameFont, bg=frameBG, fg=frameTC)
    a.name_data_label     = tk.Label(a.third_frame, text=x, font=frameFont, bg=frameBG, fg=frameTC)
    a.age_data_label      = tk.Label(a.third_frame, text=y, font=frameFont, bg=frameBG, fg=frameTC)
    a.heart_data_label    = tk.Label(a.third_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.calorie_data_label  = tk.Label(a.third_frame, text="  ", font=frameFont, bg=frameBG, fg=frameTC)
    a.heart_unit_label    = tk.Label(a.third_frame, text="bpm", font=frameFont, bg=frameBG, fg=frameTC)
    

def place_live_whidgets():
    a.first_frame.grid(row=1, column=1)
    a.power_label.grid(row=1, column=1)
    a.voltage_label.grid(row=2, column=1)
    a.current_label.grid(row=3, column=1)
    a.battery_label.grid(row=4, column=1)
    a.power_data_label.grid(row=1, column=2)
    a.voltage_data_label.grid(row=2, column=2)
    a.current_data_label.grid(row=3, column=2)
    a.battery_data_label.grid(row=4, column=2)
    a.power_unit_label.grid(row=1, column=3)
    a.voltage_unit_label.grid(row=2, column=3)
    a.current_unit_label.grid(row=3, column=3)
    a.battery_unit_label.grid(row=4, column=3)

    a.second_frame.grid(row=1, column=2)
    a.rpm_label.grid(row=1, column=1)
    a.speed_label.grid(row=2, column=1)
    a.distance_label.grid(row=3, column=1)
    a.elapsed_time.grid(row=4, column=1)
    a.rpm_data_label.grid(row=1, column=2)
    a.speed_data_label.grid(row=2, column=2)
    a.distance_data_label.grid(row=3, column=2)
    a.elapsed_data_time.grid(row=4, column=2)
    a.rpm_unit_label.grid(row=1, column=3)
    a.speed_unit_label.grid(row=2, column=3)
    a.distance_unit_label.grid(row=3, column=3)
    a.elapsed_unit_time.grid(row=4, column=3)

    a.third_frame.grid(row=1, column=3)
    a.name_label.grid(row=1, column=1)
    a.age_label.grid(row=2, column=1)
    a.heart_label.grid(row=3, column=1)
    a.calorie_label.grid(row=4, column=1)
    a.name_data_label.grid(row=1, column=2)
    a.age_data_label.grid(row=2, column=2)
    a.heart_data_label.grid(row=3, column=2)
    a.calorie_data_label.grid(row=4, column=2)
    a.heart_unit_label.grid(row=3, column=3)




border=5
frameBG='#000033'
frameTC='#FFFFFF'
frameFont='Helvetica 42'

dist_meas = 0.00
circ_cm = 66.04
km_per_hour = 0
rpm = 0
elapse = 0
sensor = 21
pulse = 0
start_timer = time.time()


a = Tk()                                 #create window
a.minsize(1600, 320)                      #size window 
a.title("Current Statistics")            #title window
a.configure(background=frameBG)        #background color   

enter_name = Label(a, text="Name", font='Helvetica 50', bg=frameBG, fg=frameTC)   #create text variable
enter_name.grid(row=1, column=1)

name_entry = Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
name_entry.grid(row=1, column=2)

enter_gender = Label(a, text="Gender", font='Helvetica 50', bg=frameBG, fg=frameTC)   #create text variable
enter_gender.grid(row=2, column=1)

gender_entry = Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
gender_entry.grid(row=2, column=2)

enter_age = Label(a, text="Age", font='Helvetica 50', bg=frameBG, fg=frameTC)   #create text variable
enter_age.grid(row=3,column=1)

age_entry = Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
age_entry.grid(row=3, column=2)

enter_weight = Label(a, text="Weight", font='Helvetica 50', bg=frameBG, fg=frameTC)   #create text variable
enter_weight.grid(row=4, column=1)

weight_entry = Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
weight_entry.grid(row=4, column=2)

enter_button = Button(a, text = "ENTER", command=click, height = 5, width = 30) #create button
enter_button.grid(row=5, column=2)


a.mainloop()