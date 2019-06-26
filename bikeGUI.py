#!bin/env python

from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)

def calculate_elapse(channel):              # callback function
    global pulse, start_timer, elapse
    pulse+=1                                # increase pulse by 1 whenever interrupt occurred
    elapse = time.time() - start_timer      # elapse for every 1 complete rotation made!
    start_timer = time.time()               # let current time equals to start_timer

def calculate_speed(r_cm):
    global pulse,elapse,rpm,dist_km,dist_meas,km_per_sec,km_per_hour
    if elapse !=0:                          # to avoid DivisionByZero error
        rpm = 1/elapse * 60
        circ_cm = (2*math.pi)*r_cm
        dist_km = circ_cm/100000            # convert cm to km
        km_per_sec = dist_km / elapse       # calculate KM/sec
        km_per_hour = km_per_sec * 3600     # calculate KM/h
        dist_meas = dist_km*pulse           # measure distance traversed in kilometer
        return km_per_hour

def init_interrupt():
    GPIO.add_event_detect(21, GPIO.FALLING, callback = calculate_elapse, bouncetime = 20)

def start_calculations(n, g, w):          #parameters are age,gender,weight
    init_interrupt()
    start = time.time()
    calories_burned = 0
    print(n,g,w)
    
    while True:
        a.update()
        heart_rate = 60.0
        calculate_speed(30.04)                 # call this function with wheel radius as parameter
        print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(rpm,km_per_hour,dist_meas,pulse))
        time.sleep(0.1)
        total_time = time.time() - start
        update_RPM_data(round(rpm,2), round(km_per_hour,2),round(dist_meas,2), round(total_time,1))
        time.sleep(0.1)
        
        
        if (g == 'm'):
            calories_burned = ((0.2017*n)+(0.1988*w)+(0.6309*heart_rate-55.0969))*(total_time/(60*4.184))
            
        if (g == 'f'):
            calories_burned = ((0.074*n)+(0.1263*w)+(0.4472*heart_rate-20.4022))*(total_time/(60*4.184))
            
        update_calorie_heart(round(calories_burned,2), round(heart_rate,2))
        time.sleep(.1)
        

def click():
    name = name_entry.get()
    gender = gender_box.get()
    age = age_box.get()
    weight = weight_box.get()
    
    age = float(age)
    weight = float(weight)
    
    if gender == 'Female':
        gender = 'f'
    if gender == 'Male':
        gender = 'm'
    
    
    live_window(name, age)
    start_calculations(age, gender, weight)

def live_window(x,y):          #parameters are name, age
    enter_name.destroy()
    enter_gender.destroy()
    enter_age.destroy()
    enter_weight.destroy()     #destroy all whidgets
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
    
def update_calorie_heart(c, h):               #parameter is calories and heart rate
    a.calorie_data_label["text"] = c
    a.heart_data_label["text"] = h

def create_live_whidgets(x,y):
    y = int(y)
    a.first_frame         = tk.LabelFrame(a, text='Power Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.power_label         = tk.Label(a.first_frame, text="power :", font=frameFont, bg=frameBG, fg=frameTC) #create power labels
    a.voltage_label       = tk.Label(a.first_frame, text="voltage :", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_label       = tk.Label(a.first_frame, text="current :", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_label       = tk.Label(a.first_frame, text="battery :", font=frameFont, bg=frameBG, fg=frameTC)
    a.power_data_label    = tk.Label(a.first_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC) #create rpm labels
    a.voltage_data_label  = tk.Label(a.first_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_data_label  = tk.Label(a.first_frame, width=10, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_data_label  = tk.Label(a.first_frame, width=10, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.power_unit_label    = tk.Label(a.first_frame, text="W", font=frameFont, bg=frameBG, fg=frameTC) #create rpm labels
    a.voltage_unit_label  = tk.Label(a.first_frame, text="V", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_unit_label  = tk.Label(a.first_frame, text="A", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_unit_label  = tk.Label(a.first_frame, text="%", font=frameFont, bg=frameBG, fg=frameTC)

    a.second_frame        = tk.LabelFrame(a, text='Speed Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.rpm_label           = tk.Label(a.second_frame, text="RPM :", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_label         = tk.Label(a.second_frame, text="speed :", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_label      = tk.Label(a.second_frame, text="distance :", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_time        = tk.Label(a.second_frame, text="time elapsed :", font=frameFont, bg=frameBG, fg=frameTC)
    a.rpm_data_label      = tk.Label(a.second_frame, width=10, text="      ", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_data_label    = tk.Label(a.second_frame, width=10,text="  ", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_data_label = tk.Label(a.second_frame, width=10,text=" ", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_data_time   = tk.Label(a.second_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.rpm_unit_label      = tk.Label(a.second_frame, text="rpm", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_unit_label    = tk.Label(a.second_frame, text="kmph", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_unit_label = tk.Label(a.second_frame, text="km", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_unit_time   = tk.Label(a.second_frame, text="s", font=frameFont, bg=frameBG, fg=frameTC)


    a.third_frame         = tk.LabelFrame(a, text='User Info', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.name_label          = tk.Label(a.third_frame, text="name :", font=frameFont, bg=frameBG, fg=frameTC)
    a.age_label           = tk.Label(a.third_frame, text="age :", font=frameFont, bg=frameBG, fg=frameTC)
    a.heart_label         = tk.Label(a.third_frame, text="heart rate :", font=frameFont, bg=frameBG, fg=frameTC)
    a.calorie_label       = tk.Label(a.third_frame, text="calories burned :", font=frameFont, bg=frameBG, fg=frameTC)
    a.name_data_label     = tk.Label(a.third_frame, width=10, text=x, font=frameFont, bg=frameBG, fg=frameTC)
    a.age_data_label      = tk.Label(a.third_frame, width=10, text=y, font=frameFont, bg=frameBG, fg=frameTC)
    a.heart_data_label    = tk.Label(a.third_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.calorie_data_label  = tk.Label(a.third_frame, width=10, text="kcal", font=frameFont, bg=frameBG, fg=frameTC)
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
frameFont='Helvetica 20'

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
pulse = 0
start_timer = time.time()


a = Tk()                                 #create window
a.pack_propagate(0)
a.minsize(420, 200)                      #size window 
a.title("Current Statistics")            #title window
a.configure(background=frameBG)        #background color

gender_box = StringVar(a)
gender_choices = ['Female', 'Male']

age_box = StringVar(a)
age_choices = [i for i in range(13,100)]

weight_box = StringVar(a)
weight_choices = [i for i in range(20,140)]

enter_name = Label(a, text="Name", font='Helvetica 20', bg=frameBG, fg=frameTC)   #create text variable
enter_name.grid(row=1, column=1)

name_entry = Entry(a, bd = 1, font='Helvetica 20')                   #create text entry box
name_entry.grid(row=1, column=2)

enter_gender = Label(a, text="M/F", font='Helvetica 20', bg=frameBG, fg=frameTC)   #create text variable
enter_gender.grid(row=2, column=1)

gender_entry = OptionMenu(a, gender_box, *gender_choices)                   #create text entry box
gender_entry.grid(row=2, column=2)
gender_box.set('Female')

enter_age = Label(a, text="Age", font='Helvetica 20', bg=frameBG, fg=frameTC)   #create text variable
enter_age.grid(row=3,column=1)

age_entry = OptionMenu(a, age_box, *age_choices)                   #create text entry box
age_entry.grid(row=3, column=2)
age_box.set('13')

enter_weight = Label(a, text="Weight(kg)", font='Helvetica 20', bg=frameBG, fg=frameTC)   #create text variable
enter_weight.grid(row=4, column=1)

weight_entry = OptionMenu(a, weight_box, *weight_choices)                   #create text entry box
weight_entry.grid(row=4, column=2)
weight_box.set(20)

enter_button = Button(a, text = "ENTER", command=click, height = 3, width = 15) #create button
enter_button.grid(row=5, column=2)


a.mainloop()