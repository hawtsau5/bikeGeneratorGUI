import tkinter as tk
import bimpy
import random

from data_handler.datas import Data

class UserInputApplication(tk.Frame):
    def __init__(self, data, master=None):
        super().__init__(master)
        super().configure(bg="navy")
        self.pack()
        self.data = data

        self.gender_var = tk.IntVar(value=random.randint(0, 1))

        self.age_var    = tk.IntVar(value=random.randint(10, 100))
        self.age_text   = tk.StringVar(value=str(self.age_var.get()))

        self.weight_var = tk.IntVar(value=random.randint(17, 190))
        self.weight_text = tk.StringVar(value=str(self.weight_var.get()))
        
        self.name_validity = True
        self.age_validity = True
        self.weight_validity = True

        self.__add_widget()
        self.__draw_widget()

    def __add_widget(self):
        self.enter_name   = tk.Label  (self, text="Name",   font="Helvetica 28", width=8, bg="navy", fg="white")
        self.enter_gender = tk.Label  (self, text="Gender", font="Helvetica 28", width=8, bg="navy", fg="white")
        self.enter_age    = tk.Label  (self, text="Age",    font="Helvetica 28", width=8, bg="navy", fg="white")
        self.enter_weight = tk.Label  (self, text="Weight", font="Helvetica 28", width=8, bg="navy", fg="white")

        self.name_entry   = tk.Entry   (self, bd=1, font="Helvetica 22",
                                        width=23, relief=tk.SUNKEN, bg="RoyalBlue3", fg="white",
                                        highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")

        self.age_btn_d10   = tk.Button (self, text="-10", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.age_var, -10))
        self.age_btn_d1   = tk.Button  (self, text="-1", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.age_var, -1))

        self.age_entry    = tk.Entry   (self, bd=1, font="Helvetica 22", textvariable=self.age_text,
                                        width=3, relief=tk.SUNKEN, bg="RoyalBlue3", fg="white",
                                        highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")

        self.age_btn_u1   = tk.Button  (self, text="+1", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.age_var, +1))
        self.age_btn_u10   = tk.Button (self, text="+10", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.age_var, +10))

        self.weight_btn_d10   = tk.Button (self, text="-10", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.weight_var, -10))
        self.weight_btn_d1   = tk.Button  (self, text="-1", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.weight_var, -1))

        self.weight_entry    = tk.Entry   (self, bd=1, font="Helvetica 22", textvariable=self.weight_text,
                                        width=3, relief=tk.SUNKEN, bg="RoyalBlue3", fg="white",
                                        highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")

        self.weight_btn_u1   = tk.Button  (self, text="+1", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.weight_var, +1))
        self.weight_btn_u10   = tk.Button (self, text="+10", font="Helvetica 14",
                                        command=lambda: self.__increment_button(self.weight_var, +10))

        self.gend_male_rb = tk.Radiobutton (self, text="Male", variable=self.gender_var, bd=6,
                                            value=False, indicatoron=0, font="Helvetica 28", width=13,
                                            bg="RoyalBlue1", fg="white", selectcolor="RoyalBlue3",
                                            activebackground="RoyalBlue3", activeforeground="white")
        self.gend_feml_rb = tk.Radiobutton (self, text="Female", variable=self.gender_var, bd=6,
                                            value=True, indicatoron=0, font="Helvetica 28", width=13,
                                            bg="RoyalBlue1", fg="white", selectcolor="RoyalBlue3",
                                            activebackground="RoyalBlue3", activeforeground="white")

        self.enter_button = tk.Button (self, text="Let's Exercise !", font="Helvetica 28", width=26, command=self.__generate_data)

    def __increment_button(self, var, value):
        var.set(int(var.get()) + value)

        if(self.age_var.get() <= 9):
            self.age_var.set(9)
        elif(self.age_var.get() >= 100):
            self.age_var.set(100)

        if(self.weight_var.get() <= 16):
            self.weight_var.set(16)
        elif(self.weight_var.get() >= 200):
            self.weight_var.set(200)

        self.age_text.set(self.age_var.get())
        self.weight_text.set(self.weight_var.get())

        self.update()
        self.master.update()

    def __draw_widget(self):
        self.enter_name.grid   (row=1, column=1, pady=10)
        self.enter_gender.grid (row=2, column=1, pady=10, rowspan=2)
        self.enter_age.grid    (row=4, column=1, pady=10)
        self.enter_weight.grid (row=5, column=1, pady=10)

        self.name_entry.grid   (row=1, column=2, pady=10, columnspan=10)

        self.age_btn_d10.grid  (row=4, column=4, pady=10)
        self.age_btn_d1.grid   (row=4, column=5, pady=10)
        self.age_entry.grid    (row=4, column=6, pady=10)
        self.age_btn_u1.grid   (row=4, column=7, pady=10)
        self.age_btn_u10.grid  (row=4, column=8, pady=10)

        self.weight_btn_d10.grid  (row=5, column=4, pady=10)
        self.weight_btn_d1.grid   (row=5, column=5, pady=10)
        self.weight_entry.grid    (row=5, column=6, pady=10)
        self.weight_btn_u1.grid   (row=5, column=7, pady=10)
        self.weight_btn_u10.grid  (row=5, column=8, pady=10)

        self.gend_male_rb.grid (row=2, column=2, columnspan=10)
        self.gend_feml_rb.grid (row=3, column=2, columnspan=10)
        
        self.enter_button.grid (row=6, column=1, padx=20, pady=10, columnspan=10)

    def __generate_data(self):
        self.__check_input_validity()
        self.__draw_errors()

        if self.name_validity and self.age_validity and self.weight_validity:
            self.data.name = str(self.name_entry.get())
            self.data.gender = bool(self.gender_var.get())
            self.data.age = int(self.age_var.get())
            self.data.weight = int(self.weight_entry.get())
            self.master.destroy()
            return

        self.update()
        self.master.update()

    def __draw_errors(self):
        if self.name_validity:
            self.name_entry.configure(bg="RoyalBlue3", fg="white",
                                        highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")
        else:
            self.name_entry.configure(bd=3, bg="red")

        if self.age_validity:
            self.age_entry.configure(bg="RoyalBlue3", fg="white",
                                    highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")
        else:
            self.age_entry.configure(bd=3, bg="red")

        if self.weight_validity:
            self.weight_entry.configure(bg="RoyalBlue3", fg="white",
                                        highlightcolor="RoyalBlue1", highlightbackground="RoyalBlue3")
        else:
            self.weight_entry.configure(bd=3, bg="red")

    def __check_input_validity(self):
        num = "1234567890"
        wildcard = "~!@#$%^&*()_+``{}|\\;':\"<>?,./"
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        self.name_validity = True
        self.age_validity = True
        self.weight_validity = True

        for i in num+wildcard:
            if i in str(self.name_entry.get()) or len(str(self.name_entry.get().replace(" ", ""))) == 0:
                self.name_validity = False

        for i in wildcard+alphabet+alphabet.upper():
            if  i in str(self.age_var.get()) or \
                i in str(self.age_text.get()) or \
                i in str(self.age_entry.get()):
                self.age_validity = False
            
            if  i in str(self.weight_var.get()) or \
                i in str(self.weight_text.get()) or \
                i in str(self.weight_entry.get()):
                self.weight_validity = False