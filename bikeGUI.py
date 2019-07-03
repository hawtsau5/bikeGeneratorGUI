#!bin/env python3

from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import math
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)


#function definitions
def calculate_elapse(channel):              # callback function
    global pulse, start_timer, elapse
    pulse += 1                                # increase pulse by 1 whenever interrupt occurred
    elapse = time.time() - start_timer      # elapse for every 1 complete rotation made!
    start_timer = time.time()               # let current time equals to start_timer

def calculate_speed(r_cm):                    #calculates speed in kmph from rpm based on wheel radius
    global pulse,elapse,rpm,dist_km,dist_meas,km_per_sec,km_per_hour
    if elapse != 0:                              # to avoid DivisionByZero error
        rpm = 1 / elapse * 60
        circ_cm = (2 * math.pi) * r_cm
        dist_km = circ_cm / 100000              # convert cm to km
        km_per_sec = dist_km / elapse           # calculate KM/sec
        km_per_hour = km_per_sec * 3600         # calculate KM/h
        dist_meas = dist_km * pulse             # measure distance traversed in kilometer
        return km_per_hour

def init_interrupt():                     #initiate sensor readings
    GPIO.add_event_detect(21, GPIO.FALLING, callback = calculate_elapse, bouncetime = 20)

def start_calculations(age, gender, weight):          #parameters are age,gender,weight
    init_interrupt()                             #start rpm sensor calculations
    start = time.time()
    calories_burned = 0
    print(age, gender, weight)

    while True:
        heart_rate = 60.0
        calculate_speed(30.04)                 # call this to get speed in kmph
        print("rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}".format(rpm,km_per_hour,dist_meas,pulse))
        time.sleep(0.1)
        total_time = time.time() - start
        update_RPM_data(round(rpm,2), round(km_per_hour,2),round(dist_meas,2), round(total_time,1))  #update rpm data labels
        time.sleep(0.1)
        
        
        #calculate calories burned based on gender, age, weight and update data labels
        if (gender == 'm'):
            calories_burned = ((0.2017*age)+(0.1988*weight)+(0.6309*heart_rate-55.0969))*(total_time/(60*4.184))
        else:
            calories_burned = ((0.074*age)+(0.1263*weight)+(0.4472*heart_rate-20.4022))*(total_time/(60*4.184))

        update_calorie_heart(round(calories_burned,2), round(heart_rate,2))
        time.sleep(.1)

        main_window.update()

def click():                      #define action on pressing "ENTER" button
    name = name_entry.get()               #store name, gender,age, weight from user entries
    gender = ["f", "m"][gender_var.get()]
    age = age_var.get()
    weight = weight_var.get()

    age = float(age)            #convert age and weight to float for calories burned calculations
    weight = float(weight)


    live_window(name, age)                #call live window to create updating screen
    start_calculations(age, gender, weight)#start rpm sensor and calorie calculations

def live_window(n, a):          #parameters are name, age
    phantom_column.destroy()
    enter_name.destroy()
    enter_gender.destroy()
    enter_age.destroy()
    enter_weight.destroy()     #destroy all whidgets
    enter_button.destroy()
    name_entry.destroy()
    age_entry.destroy()
    weight_entry.destroy()
    gend_feml_rb.destroy()
    gend_male_rb.destroy()
    age_btn_d1.destroy()
    age_btn_u1.destroy()
    weight_btn_d1.destroy()
    weight_btn_u1.destroy()

    create_live_whidgets(n,a)   #create live window with updating labels
    place_live_whidgets()


def update_RPM_data(rpm, speed, distance, time):             #parameters are rpm, speed, distance, time
    main_window.rpm_data_label["text"] = rpm                 #updates rpm speed distnce and time data labels
    main_window.speed_data_label["text"] = speed
    main_window.distance_data_label["text"] = distance
    main_window.elapsed_data_time["text"] = time


def update_calorie_heart(calorie, heart_rate):               #parameters are calories and heart rate
    main_window.calorie_data_label["text"] = str(calorie)    #updates calorie and heart rate data labels
    main_window.heart_data_label["text"] = str(heart_rate)


def create_live_whidgets(name: str, age: int):                 #create whidegets for live statistics
    main_window.first_frame         = tk.LabelFrame(main_window, text='Power Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frame_titleTC)
    main_window.power_label         = tk.Label(main_window.first_frame, text="power :", font=frameFont, bg=frameBG, fg=frameTC) #create power labels
    main_window.voltage_label       = tk.Label(main_window.first_frame, text="voltage :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.current_label       = tk.Label(main_window.first_frame, text="current :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.battery_label       = tk.Label(main_window.first_frame, text="battery :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.power_data_label    = tk.Label(main_window.first_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.voltage_data_label  = tk.Label(main_window.first_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.current_data_label  = tk.Label(main_window.first_frame, width=10, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.battery_data_label  = tk.Label(main_window.first_frame, width=10, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.power_unit_label    = tk.Label(main_window.first_frame, text="W", font=frameFont, bg=frameBG, fg=frameTC) 
    main_window.voltage_unit_label  = tk.Label(main_window.first_frame, text="V", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.current_unit_label  = tk.Label(main_window.first_frame, text="A", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.battery_unit_label  = tk.Label(main_window.first_frame, text="%", font=frameFont, bg=frameBG, fg=frameTC)

    main_window.second_frame        = tk.LabelFrame(main_window, text='Speed Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frame_titleTC)#create rpm labels
    main_window.rpm_label           = tk.Label(main_window.second_frame, text="RPM :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.speed_label         = tk.Label(main_window.second_frame, text="speed :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.distance_label      = tk.Label(main_window.second_frame, text="distance :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.elapsed_time        = tk.Label(main_window.second_frame, text="time elapsed :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.rpm_data_label      = tk.Label(main_window.second_frame, width=10, text="      ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.speed_data_label    = tk.Label(main_window.second_frame, width=10,text="  ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.distance_data_label = tk.Label(main_window.second_frame, width=10,text=" ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.elapsed_data_time   = tk.Label(main_window.second_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.rpm_unit_label      = tk.Label(main_window.second_frame, text="rpm", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.speed_unit_label    = tk.Label(main_window.second_frame, text="kmph", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.distance_unit_label = tk.Label(main_window.second_frame, text="km", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.elapsed_unit_time   = tk.Label(main_window.second_frame, text="s", font=frameFont, bg=frameBG, fg=frameTC)

    main_window.third_frame         = tk.LabelFrame(main_window, text='User Info', font='Helvetica 22', bd=border, bg=frameBG, fg=frame_titleTC)#create user info labels
    main_window.name_label          = tk.Label(main_window.third_frame, text="name :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.age_label           = tk.Label(main_window.third_frame, text="age :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.heart_label         = tk.Label(main_window.third_frame, text="heart rate :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.calorie_label       = tk.Label(main_window.third_frame, text="calories burned :", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.name_data_label     = tk.Label(main_window.third_frame, width=10, text=name, font=frameFont, bg=frameBG, fg=frameTC)
    main_window.age_data_label      = tk.Label(main_window.third_frame, width=10, text=int(age), font=frameFont, bg=frameBG, fg=frameTC)
    main_window.heart_data_label    = tk.Label(main_window.third_frame, width=10, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.calorie_data_label  = tk.Label(main_window.third_frame, width=10, text="kcal", font=frameFont, bg=frameBG, fg=frameTC)
    main_window.heart_unit_label    = tk.Label(main_window.third_frame, text="bpm", font=frameFont, bg=frameBG, fg=frameTC)


def place_live_whidgets():                                        #places whidgets in window
    main_window.first_frame.pack(side=TOP, fill=Y, expand=NO)
    main_window.power_label.grid(row=1, column=1)
    main_window.voltage_label.grid(row=2, column=1)
    main_window.current_label.grid(row=3, column=1)
    main_window.battery_label.grid(row=4, column=1)
    main_window.power_data_label.grid(row=1, column=2)
    main_window.voltage_data_label.grid(row=2, column=2)
    main_window.current_data_label.grid(row=3, column=2)
    main_window.battery_data_label.grid(row=4, column=2)
    main_window.power_unit_label.grid(row=1, column=3)
    main_window.voltage_unit_label.grid(row=2, column=3)
    main_window.current_unit_label.grid(row=3, column=3)
    main_window.battery_unit_label.grid(row=4, column=3)

    main_window.second_frame.pack(fill=Y, expand=NO)
    main_window.rpm_label.grid(row=1, column=1)
    main_window.speed_label.grid(row=2, column=1)
    main_window.distance_label.grid(row=3, column=1)
    main_window.elapsed_time.grid(row=4, column=1)
    main_window.rpm_data_label.grid(row=1, column=2)
    main_window.speed_data_label.grid(row=2, column=2)
    main_window.distance_data_label.grid(row=3, column=2)
    main_window.elapsed_data_time.grid(row=4, column=2)
    main_window.rpm_unit_label.grid(row=1, column=3)
    main_window.speed_unit_label.grid(row=2, column=3)
    main_window.distance_unit_label.grid(row=3, column=3)
    main_window.elapsed_unit_time.grid(row=4, column=3)

    main_window.third_frame.pack(fill=Y, expand=NO)
    main_window.name_label.grid(row=1, column=1)
    main_window.age_label.grid(row=2, column=1)
    main_window.heart_label.grid(row=3, column=1)
    main_window.calorie_label.grid(row=4, column=1)
    main_window.name_data_label.grid(row=1, column=2)
    main_window.age_data_label.grid(row=2, column=2)
    main_window.heart_data_label.grid(row=3, column=2)
    main_window.calorie_data_label.grid(row=4, column=2)
    main_window.heart_unit_label.grid(row=3, column=3)


def __increment_button(var, value):
        var.set(int(var.get()) + value)

        if(int(age_var.get()) <= 9):
            age_var.set(str(9))
        elif(int(age_var.get()) >= 100):
            age_var.set(str(100))

        if(int(weight_var.get()) <= 16):
            weight_var.set(str(16))
        elif(int(weight_var.get()) >= 200):
            weight_var.set(str(200))

        age_var.set(age_var.get())
        weight_var.set(weight_var.get())
        main_window.after(100,__increment_button)
        main_window.update()


def stop(event):
    print("halted")
    global is_running
    is_running = False


def start(event):
    print("started")
    global is_running, started_at
    is_running = True
    started_at = time.time()

    running(event)


def running(event):
    global is_running, started_at, received_at

    if is_running:

        now = time.time()

        if now - 1 > started_at:
            increase_or_decrease(event)
        main_window.after(1000, lambda event=event: running(event))


def increase_or_decrease(event):

    widget = str(event.widget)

    # decr age
    if widget == ".!button":
        print("decrease age by 10")
        __increment_button(age_var, -10)

    # incr age
    elif widget == ".!button2":
        print("increase age by 10")
        __increment_button(age_var, 10)

    # decr weight
    elif widget == ".!button3":
        print("decrease weight by 10")
        __increment_button(weight_var, -10)

    # incr weight
    elif widget == ".!button4":
        print("increase weight by 10")
        __increment_button(weight_var, 10)
    else:
        # just blow up
        raise("not implemented")

#end function definitions


border = 5                              #variables for fonts and color scheme
frameBG = '#000033'
frameTC = '#FFFFFF'
frame_titleTC = '#949BA3'
frameFont = 'Helvetica 20'

dist_meas = 0.00        #initialize variables for rpm sensor
km_per_hour = 0
rpm = 0
elapse = 0
pulse = 0
start_timer = time.time()

main_window = Tk()                                                      #create main window
w, h = main_window.winfo_screenwidth(), main_window.winfo_screenheight()   #fullscreen
main_window.geometry("%dx%d+0+0" % (w, h))        #size window to full screen
main_window.title("Current Statistics")           #title window
main_window.configure(background=frameBG)         #background color

phantom_column = Label(main_window, text="", width=48, font='Helvetica 20', bg=frameBG, fg=frameTC)    #used to center all whidgets

enter_name      = Label(main_window, text="Name", font='Helvetica 20', width=11, bg=frameBG, fg=frameTC)        #create labels for user information
enter_gender    = Label(main_window, text="M/F" , font='Helvetica 20', width=11, bg=frameBG, fg=frameTC)
enter_age       = Label(main_window, text="Age" , font='Helvetica 20', width=11, bg=frameBG, fg=frameTC)
enter_weight    = Label(main_window, text="Weight(kg)", font='Helvetica 20', width=11, bg=frameBG, fg=frameTC)
enter_button    = Button(main_window, text = "ENTER", font='Helvetica 20', command = click, width=20)

gender_var = tk.IntVar(value=0)        #create variables to set whidgets
age_var = tk.StringVar(value=13)
weight_var = tk.StringVar(value=50)

name_entry = Entry(main_window, bd = 1, font='Helvetica 20', width=20)   #create entry box to type name


gend_male_rb    = tk.Radiobutton(main_window, text="Male", variable=gender_var, bd=6,           #create radiobuttons for male/female choice
                              value=1, indicatoron=0, font="Helvetica 20", width=13,
                              bg="RoyalBlue1", fg="white", selectcolor="RoyalBlue3",
                              activebackground="RoyalBlue3", activeforeground="white")
gend_feml_rb    = tk.Radiobutton(main_window, text="Female", variable=gender_var, bd=6,
                              value=0, indicatoron=0, font="Helvetica 20", width=13,
                              bg="RoyalBlue1", fg="white", selectcolor="RoyalBlue3",
                              activebackground="RoyalBlue3", activeforeground="white")


age_btn_d1      = tk.Button(main_window, text="-", font="Helvetica 22", width=3, #create buttons to increment/decrement age by 1 and entry box to show value
                         command=lambda:   __increment_button(age_var, -1))

age_entry       = tk.Entry(main_window, bd=1, font="Helvetica 22", textvariable=age_var,
                        width=3, relief=tk.SUNKEN, bg="RoyalBlue3", fg="white",
                        highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")

age_btn_u1      = tk.Button(main_window, text="+", font="Helvetica 22", width=3,
                         command=lambda:   __increment_button(age_var, +1))

weight_btn_d1   = tk.Button(main_window, text="-", font="Helvetica 22", width=3, #create buttons to increment/decrement weight by 1 and entry box to show value
                            command=lambda:   __increment_button(weight_var, -1))

weight_entry    = tk.Entry(main_window, bd=1, font="Helvetica 22", textvariable=weight_var,
                           width=3, relief=tk.SUNKEN, bg="RoyalBlue3", fg="white",
                           highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")

weight_btn_u1 = tk.Button(main_window, text="+", font="Helvetica 22", width=3,
                            command=lambda:   __increment_button(weight_var, +1))


is_running = False
started_at = time.time()


weight_btn_u1.bind("<Button-1>", start)
weight_btn_u1.bind("<ButtonRelease-1>", stop)

weight_btn_d1.bind("<Button-1>", start)
weight_btn_d1.bind("<ButtonRelease-1>", stop)


age_btn_u1.bind("<Button-1>", start)
age_btn_u1.bind("<ButtonRelease-1>", stop)

age_btn_d1.bind("<Button-1>", start)
age_btn_d1.bind("<ButtonRelease-1>", stop)



phantom_column.grid     (row=1, column=0)                    #place all whidgets for user information
enter_name.grid         (row=1, column=1, pady=10)
enter_gender.grid       (row=2, column=1, pady=10, rowspan=2)
enter_age.grid          (row=4, column=1, pady=10)
enter_weight.grid       (row=5, column=1, pady=10)

name_entry.grid         (row=1, column=2, columnspan=10)

age_btn_d1.grid         (row=4, column=5, pady=10)
age_entry.grid          (row=4, column=6, pady=10)
age_btn_u1.grid         (row=4, column=7, pady=10)

weight_btn_d1.grid      (row=5, column=5, pady=10)
weight_entry.grid       (row=5, column=6, pady=10)
weight_btn_u1.grid      (row=5, column=7, pady=10)

gend_feml_rb.grid       (row=2, column=2, columnspan=10)
gend_male_rb.grid       (row=3, column=2, columnspan=10)

enter_button.grid       (row=6, column=1, padx=20, pady=10, columnspan=10)

main_window.mainloop()