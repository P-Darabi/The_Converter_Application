import tkinter as tk
from tkinter import E, W, N, S, ttk


win=tk.Tk()
win.title(" Converting Fahrenheit to Celsius ")

Fahrenheit= tk.Label(
    master=win,
    text="Fahrenheit:    ",
    
    )

Celsius=tk.Label(
    master=win,
    text="Celsius:  ",
    
)

Result=tk.Label(
    master=win,
    text=" You should enter a number ",
)

entry=ttk.Entry(
    master=win,
    width=60,

)

def calculate_button(*args):
    try:
       Result["text"]= (float(entry.get())-32)/1.8
    except ValueError:
        if entry.get()!="":
            Result["text"]= "You should enter a number."
        else:
            Result["text"]= "You enter no number."    

Calc=ttk.Button(
    master=win,
    text="Calc",
    width=10,
    command=calculate_button, 
)

win.bind("<Return>", calculate_button)

Fahrenheit.grid(row=1,column=0,sticky=(W,),padx=10,pady=10)
Celsius.grid(row=2,column=0, sticky=(W,),padx=10,pady=10)
entry.grid(row=1,column=1)
Result.grid(row=2,column=1,columnspan=2, padx=10,pady=10,sticky=(W,))
Calc.grid(row=1,column=2,padx=10,pady=10)
win.mainloop()