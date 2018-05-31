from most_popular_language import *
from db import *
from people import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

#
#most_popular_language()

#read_data()

root = Tk()
root.title("Coursework")
root.geometry("400x300+300+250")
# count  = IntVar()
# count_label = Label(text="Введіть  кількість даних:")
# count_label.grid(row=1, column=0, sticky="w")
# count_entry = Entry(textvariable=count)
# count_entry.grid(row=1, column=1, padx=5, pady=5)
result_data = Button(text="Записати дані у БД", command=read_data)
result_data.grid(row=0, column=1, padx=5, pady=5, sticky="e")

gen_data = Button(text="Згенерувати дані", command=generate_data)
gen_data.grid(row=2, column=1, padx=5, pady=5, sticky="e")

plot = Button(text="Графік 1", command=most_popular_language)
plot.grid(row=3, column=1, padx=5, pady=5, sticky="e")

plot1 = Button(text="Графік 2", command=people)
plot1.grid(row=4, column=1, padx=5, pady=5, sticky="e")
#
root.mainloop()