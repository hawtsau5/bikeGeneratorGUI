import tkinter as tk
import bimpy

class UserInputApplication(tk.Tk()):
    def __init__(self):
        pass

    def draw_widget(self):
        a = tk.Tk()                                 #create window
        a.minsize(1600, 320)                      #size window 
        a.title("Current Statistics")            #title window
        a.configure()        #background color   

        enter_name = tk.Label(a, text="Name", font='Helvetica 50')   #create text variable
        enter_name.grid(row=1, column=1)

        name_entry = tk.Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
        name_entry.grid(row=1, column=2)

        enter_gender = tk.Label(a, text="Gender", font='Helvetica 50')   #create text variable
        enter_gender.grid(row=2, column=1)

        gender_entry = tk.Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
        gender_entry.grid(row=2, column=2)

        enter_age = tk.Label(a, text="Age", font='Helvetica 50')   #create text variable
        enter_age.grid(row=3,column=1)

        age_entry = tk.Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
        age_entry.grid(row=3, column=2)

        enter_weight = tk.Label(a, text="Weight", font='Helvetica 50')   #create text variable
        enter_weight.grid(row=4, column=1)

        weight_entry = tk.Entry(a, bd = 10, font='Helvetica 50')                   #create text entry box
        weight_entry.grid(row=4, column=2)

        enter_button = tk.Button(a, text = "ENTER", height = 5, width = 30) #create button
        enter_button.grid(row=5, column=2)

        a.mainloop()
