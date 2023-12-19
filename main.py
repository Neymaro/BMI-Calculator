from tkinter import *

def calculator():
    kg = int(weight_entry.get())
    hg = int(height_entry.get())/100
    bmi = float(kg / (hg*hg))
    if bmi >= 30:
        result["text"] = "Obesity"
    elif 25 <= bmi < 29:
        result["text"] = "Overweight"
    elif 18.5 < bmi < 24:
        result["text"] = "Overweight"
    elif bmi <= 18.4:
        result["text"] = "Overweight"

window = Tk()
window.title("BMI Calculator")
window.minsize(width=280,height=220)

label = Label(text="BMI Calculator")
label.pack(pady=10)

label = Label(text="Enter Your Width")
label.pack()

weight_entry = Entry(window, width=20)
weight_entry.pack(pady=10)

label = Label(text="Enter Your Height")
label.pack()

height_entry = Entry(window, width=20)
height_entry.pack(pady=10)

calculate_button = Button(window, text="Calculate", command=calculator)
calculate_button.pack()

result = Label(text="ENTER YOUR WEIGHT & HEIGHT")
result.pack()

window.mainloop()