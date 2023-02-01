from brain_code import Grading
from tkinter import *

window = Tk()
window.title("Grade Point Calculator")
window.minsize(600, 600)
window.config(padx=50, pady=50)
brain = Grading()
names = []
names2 = []
names3 = []
scores = []
scores2 = []
scores3 = []
RED = "#e7305b"
GREEN = "#9bdeac"

def get_course():
    #print(spin_one.get())
    Number = int(spin_one.get())
    for i in range(Number):
        n = Entry()
        names.append(n)
        n.grid(column=0, row=2+i)



def get_course2():
    print(spin_two.get())
    Number = int(spin_two.get())
    for i in range(Number):
        n = Entry()
        names2.append(n)
        n.grid(column=2, row=2 + i)

def get_course3():
    print(spin_three.get())
    Number = int(spin_three.get())
    for i in range(Number):
        n = Entry()
        names3.append(n)
        n.grid(column=4, row=2 + i)

def work_on():
    ones = 0
    twos = 0
    threes = 0
    total = 0
    for i in brain.one_units:
        a = brain.grade_pointsno(int(i))
        total += a
        ones += 1

    for i in brain.two_units:
        a = brain.grade_pointsno(int(i))
        total += a * 2
        twos += 2

    for i in brain.three_units:
        a = brain.grade_pointsno(int(i))
        total += a * 3
        threes += 3

    Gp = total / (ones + threes + twos)
    if Gp >= 3:
        label_five.config(fg=GREEN)
    else:
        label_five.config(fg=RED)
    label_five.config(text=f"{Gp}")

def when_done():
    for i in names:
        print(i.get())
        scores.append(i.get())
        brain.one_units.append(i.get())
        #brain.grade_points(int(i.get()))
    for i in names2:
        scores2.append(i.get())
        brain.two_units.append(i.get())
        #brain.grade_points(int(i.get()))
    for i in names3:
        scores3.append(i.get())
        brain.three_units.append(i.get())
        #brain.grade_points(int(i.get()))
    print(brain.grades)
    work_on()






label_one = Label(text="Number of one units:")
label_one.config(padx=10, pady=10)
label_one.grid(column=0, row=0)
spin_one = Spinbox(from_=0, to=10, width=2)
spin_one.grid(column=1, row=0)
label_two = Label(text="Number of two units:")
label_two.config(padx=10, pady=10)
label_two.grid(column=2, row=0)
spin_two = Spinbox(from_=0, to=10, width=2)
spin_two.grid(column=3, row=0)

label_three = Label(text="Number of three units:")
label_three.config(padx=10, pady=10)
label_three.grid(column=4, row=0)

spin_three = Spinbox(from_=0, to=10, width=2)
spin_three.grid(column=5, row=0)
button1 = Button(text="Done", command=get_course)
button1.config(padx=10, pady=10)
button1.grid(column=0, row=1)
button2 = Button(text="Done", command=get_course2)
button2.config(padx=10, pady=10)
button2.grid(column=2, row=1)
button3 = Button(text="Done", command=get_course3)
button3.config(padx=10, pady=10)
button3.grid(column=4, row=1)
button4 = Button(text="Compute", command=when_done)
button4.grid(column=0, row=14)

label_four = Label(text="Your GP is")
label_four.grid(column=3, row=14)
label_five = Label(text="0")
label_five.grid(column=4, row=14)

window.mainloop()