import tkinter as tk
import mainGPIO


live_data = mainGPIO.LiveData()

def click():
    name = nameEntry.get()
    age = ageEntry.get()
    liveWindow(name, age)

def liveWindow(x,y):
    enterName.destroy()                         
    enterAge.destroy()                     #destroy all whidgets
    enterButton.destroy()                            
    nameEntry.destroy()
    ageEntry.destroy()

    createLiveWidgets(x,y)
    placeLiveWidgets()

    while True:
        live_data.get_rpm()

def createLiveWidgets(x,y):
    a.first_frame = tk.LabelFrame(a, text='Power Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.power_label        = tk.Label(a.first_frame, text="power :", font=frameFont, bg=frameBG, fg=frameTC) #create power labels
    a.voltage_label      = tk.Label(a.first_frame, text="voltage :", font=frameFont, bg=frameBG, fg=frameTC)
    a.current_label     = tk.Label(a.first_frame, text="current :", font=frameFont, bg=frameBG, fg=frameTC)
    a.battery_label     = tk.Label(a.first_frame, text="battery :", font=frameFont, bg=frameBG, fg=frameTC)
    a.powerData_label        = tk.Label(a.first_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC) #create rpm labels
    a.voltageData_label      = tk.Label(a.first_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.currentData_label     = tk.Label(a.first_frame, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.batteryData_label     = tk.Label(a.first_frame, text="    ", font=frameFont, bg=frameBG, fg=frameTC)
    a.powerUnit_label        = tk.Label(a.first_frame, text="W", font=frameFont, bg=frameBG, fg=frameTC) #create rpm labels
    a.voltageUnit_label      = tk.Label(a.first_frame, text="V", font=frameFont, bg=frameBG, fg=frameTC)
    a.currentUnit_label     = tk.Label(a.first_frame, text="A", font=frameFont, bg=frameBG, fg=frameTC)
    a.batteryUnit_label     = tk.Label(a.first_frame, text="%", font=frameFont, bg=frameBG, fg=frameTC)

    a.second_frame = tk.LabelFrame(a, text='Speed Levels', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.rpm_label              = tk.Label(a.second_frame, text="RPM :", font=frameFont, bg=frameBG, fg=frameTC)
    a.speed_label            = tk.Label(a.second_frame, text="speed :", font=frameFont, bg=frameBG, fg=frameTC)
    a.distance_label              = tk.Label(a.second_frame, text="distance :", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsed_time          = tk.Label(a.second_frame, text="time elapsed :", font=frameFont, bg=frameBG, fg=frameTC)
    a.rpmData_label              = tk.Label(a.second_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.speedData_label            = tk.Label(a.second_frame, text="  ", font=frameFont, bg=frameBG, fg=frameTC)
    a.distanceData_label              = tk.Label(a.second_frame, text=" ", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsedData_time          = tk.Label(a.second_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.rpmUnit_label              = tk.Label(a.second_frame, text="rpms", font=frameFont, bg=frameBG, fg=frameTC)
    a.speedUnit_label            = tk.Label(a.second_frame, text="mph", font=frameFont, bg=frameBG, fg=frameTC)
    a.distanceUnit_label              = tk.Label(a.second_frame, text="m", font=frameFont, bg=frameBG, fg=frameTC)
    a.elapsedUnit_time          = tk.Label(a.second_frame, text="s", font=frameFont, bg=frameBG, fg=frameTC)


    a.third_frame = tk.LabelFrame(a, text='User Info', font='Helvetica 22', bd=border, bg=frameBG, fg=frameTC)
    a.name_label              = tk.Label(a.third_frame, text="name :", font=frameFont, bg=frameBG, fg=frameTC)
    a.age_label            = tk.Label(a.third_frame, text="age :", font=frameFont, bg=frameBG, fg=frameTC)
    a.heart_label        = tk.Label(a.third_frame, text="heart rate :", font=frameFont, bg=frameBG, fg=frameTC)
    a.calorie_label   = tk.Label(a.third_frame, text="calories burned :", font=frameFont, bg=frameBG, fg=frameTC)
    a.nameData_label              = tk.Label(a.third_frame, text=x, font=frameFont, bg=frameBG, fg=frameTC)
    a.ageData_label            = tk.Label(a.third_frame, text=y, font=frameFont, bg=frameBG, fg=frameTC)
    a.heartData_label        = tk.Label(a.third_frame, text="   ", font=frameFont, bg=frameBG, fg=frameTC)
    a.calorieData_label   = tk.Label(a.third_frame, text="  ", font=frameFont, bg=frameBG, fg=frameTC)
    a.heartUnit_label        = tk.Label(a.third_frame, text="bpm", font=frameFont, bg=frameBG, fg=frameTC)
    

def placeLiveWidgets():
    a.first_frame.grid(row=1, column=1)
    a.power_label.grid(row=1, column=1)
    a.voltage_label.grid(row=2, column=1)
    a.current_label.grid(row=3, column=1)
    a.battery_label.grid(row=4, column=1)
    a.powerData_label.grid(row=1, column=2)
    a.voltageData_label.grid(row=2, column=2)
    a.currentData_label.grid(row=3, column=2)
    a.batteryData_label.grid(row=4, column=2)
    a.powerUnit_label.grid(row=1, column=3)
    a.voltageUnit_label.grid(row=2, column=3)
    a.currentUnit_label.grid(row=3, column=3)
    a.batteryUnit_label.grid(row=4, column=3)

    a.second_frame.grid(row=1, column=2)
    a.rpm_label.grid(row=1, column=1)
    a.speed_label.grid(row=2, column=1)
    a.distance_label.grid(row=3, column=1)
    a.elapsed_time.grid(row=4, column=1)
    a.rpmData_label.grid(row=1, column=2)
    a.speedData_label.grid(row=2, column=2)
    a.distanceData_label.grid(row=3, column=2)
    a.elapsedData_time.grid(row=4, column=2)
    a.rpmUnit_label.grid(row=1, column=3)
    a.speedUnit_label.grid(row=2, column=3)
    a.distanceUnit_label.grid(row=3, column=3)
    a.elapsedUnit_time.grid(row=4, column=3)

    a.third_frame.grid(row=1, column=3)
    a.name_label.grid(row=1, column=1)
    a.age_label.grid(row=2, column=1)
    a.heart_label.grid(row=3, column=1)
    a.calorie_label.grid(row=4, column=1)
    a.nameData_label.grid(row=1, column=2)
    a.ageData_label.grid(row=2, column=2)
    a.heartData_label.grid(row=3, column=2)
    a.calorieData_label.grid(row=4, column=2)
    a.heartUnit_label.grid(row=3, column=3)
    

border=5
frameBG='#000033'
frameTC='#FFFFFF'
frameFont='Helvetica 42'


a = tk.Tk()                                 #create window
a.minsize(1490, 320)                      #size window 
a.title("Current Statistics")            #title window
a.configure(background=frameBG)        #background color   

enterName = tk.Label(a, text="Name", font='Helvetica 50', bg=frameBG, fg=frameTC)   #create text variable
enterName.grid(row=1, column=1)

nameEntry = tk.Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
nameEntry.grid(row=1, column=2)


enterAge = tk.Label(a, text="Age", font='Helvetica 50', bg=frameBG, fg=frameTC)   #create text variable
enterAge.grid(row=2,column=1)

ageEntry = tk.Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
ageEntry.grid(row=2, column=2)

enterButton = tk.Button(a, text = "ENTER", command=click, height = 5, width = 30) #create button
enterButton.grid(row=3, column=2)


a.mainloop() 