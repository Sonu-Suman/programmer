from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry('387x403')
root.maxsize(387, 403)
root.minsize(387, 403)

e = Entry(root, width=40, borderwidth=5, fg='red', bg='gray')
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

global f_num


# e.insert(0, "Enter your name here: ")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clean():
    e.delete(0, END)


def button_sum():
    first_number = e.get()
    global f_num, math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num, math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def button_mult():
    first_number = e.get()
    global f_num, math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num, math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


def button_per():
    first_number = e.get()
    global f_num, math
    math = 'percentage'
    f_num = int(first_number)
    e.delete(0, END)


def button_square():
    first_number = e.get()
    global f_num, math
    math = 'square'
    f_num = int(first_number)
    e.delete(0, END)
    pass


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + int(second_number))

    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))

    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))

    if math == 'division':
        e.insert(0, f_num / int(second_number))

    if math == 'square':
        e.insert(0, f_num ** int(second_number))

    if math == 'percentage':
        e.insert(0, str((int(second_number) * 100) / f_num) + '%')


button_1 = Button(root, text='1', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(1), bg='pink', fg='red')
button_2 = Button(root, text='2', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(2), bg='pink', fg='blue')
button_3 = Button(root, text='3', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(3), bg='pink', fg='green')
button_4 = Button(root, text='4', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(4), bg='pink', fg='black')
button_5 = Button(root, text='5', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(5), bg='pink', fg='gray')
button_6 = Button(root, text='6', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(6), bg='pink', fg='light blue')
button_7 = Button(root, text='7', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(7), bg='pink', fg='red')
button_8 = Button(root, text='8', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(8), bg='pink', fg='orange')
button_9 = Button(root, text='9', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(9), bg='pink', fg='black')
button_0 = Button(root, text='0', padx=40, pady=20, relief=RIDGE, command=lambda: button_click(0), bg='pink', fg='gray')

button_equal = Button(root, text='=', padx=85, pady=20, command=button_equal, bg='orange', relief=RIDGE, borderwidth=3, fg='blue')
button_clear = Button(root, text='Clear', padx=75, pady=20, command=button_clean, bg='yellow', relief=RIDGE, borderwidth=3, fg='red')

button_add = Button(root, text='+', padx=39, pady=20, command=button_sum, bg='blue', relief=RIDGE, borderwidth=3)
button_subtract = Button(root, text='--', padx=37, pady=20, command=button_sub, bg='blue', relief=RIDGE, borderwidth=3)
button_multiply = Button(root, text='X', padx=40, pady=20, command=button_mult, bg='blue', relief=RIDGE, borderwidth=3)
button_divide = Button(root, text='/', padx=40, pady=20, command=button_div, bg='blue', relief=RIDGE, borderwidth=3)

# Currency converter
button_squar = Button(root, text="^", padx=39, pady=20, command=button_square, bg='light blue', relief=RIDGE, borderwidth=4)
# button_pound = Button(root, text="€", padx=40, pady=20, command=button_pou)
button_percentage = Button(root, text='%', padx=38, pady=20, command=button_per, bg='light blue', relief=RIDGE, borderwidth=4)

# put button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=2)

button_clear.grid(row=4, column=0, columnspan=2)

button_equal.grid(row=5, column=0, columnspan=2)

button_add.grid(row=4, column=3)
button_subtract.grid(row=1, column=3)
button_divide.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)

# Other button
button_squar.grid(row=5, column=3)
button_percentage.grid(row=5, column=2)
# button_dollar.grid(row=6, column=1)


root.mainloop()