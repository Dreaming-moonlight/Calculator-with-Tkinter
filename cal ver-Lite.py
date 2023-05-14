import tkinter
from tkinter import *
import customtkinter as tk

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

app = tk.CTk()
app.geometry('435x680')

def button_function():
    print("button pressed")

button = tk.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

first_number=second_number=operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number, operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number, second_number, operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    elif operator == 'x^2':
        result_label.config(text=str(first_number * first_number))
    elif operator == 'Area':
        result_label.config(text=str(first_number * second_number))
    elif operator == 'C/$':
        result_label.config(text=str(first_number / 80))
    elif operator == 'C/₹':
        result_label.config(text=str(first_number * 80))
    else:
        if second_number == 0:
            result_label.config(text="Error (ER)")
        else:
            result_label.config(text=str((first_number / second_number)))

root = Tk()
root.title('Calculator v1.0.1 Lite')
root.geometry('435x680')
root.resizable(0,0)
root.configure(background='white')

result_label = Label(root, text='', bg='#fff', fg='black')
result_label.grid(row=0, column=0, columnspan = 1000,pady=(50, 25), sticky='w')
result_label.config(font=('verdana',30,'bold'))

button_7 = Button(root, text='7', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(7))
button_7.grid(row=1, column=0)
button_7.config(font=('verdana',14))

button_8 = Button(root, text='8', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(8))
button_8.grid(row=1, column=1)
button_8.config(font=('verdana',14))

button_9 = Button(root, text='9', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(9))
button_9.grid(row=1, column=2)
button_9.config(font=('verdana',14))

button_add = Button(root, text='+', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_operator('+'))
button_add.grid(row=1, column=3)
button_add.config(font=('verdana',14))

button_4 = Button(root, text='4', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(4))
button_4.grid(row=2, column=0)
button_4.config(font=('verdana',14))

button_5 = Button(root, text='5', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(5))
button_5.grid(row=2, column=1)
button_5.config(font=('verdana',14))

button_6 = Button(root, text='6', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(6))
button_6.grid(row=2, column=2)
button_6.config(font=('verdana',14))

button_sub = Button(root, text='-', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_operator('-'))
button_sub.grid(row=2, column=3)
button_sub.config(font=('verdana',14))

button_1 = Button(root, text='1', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(1))
button_1.grid(row=3, column=0)
button_1.config(font=('verdana',14))

button_2 = Button(root, text='2', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(2))
button_2.grid(row=3, column=1)
button_2.config(font=('verdana',14))

button_3 = Button(root, text='3', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(3))
button_3.grid(row=3, column=2)
button_3.config(font=('verdana',14))

button_multiply = Button(root, text='*', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_operator('*'))
button_multiply.grid(row=3, column=3)
button_multiply.config(font=('verdana',14))

button_clear = Button(root, text='A/C', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :clear())
button_clear.grid(row=4, column=0)
button_clear.config(font=('verdana',14))

button_0 = Button(root, text='0', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_digit(0))
button_0.grid(row=4, column=1)
button_0.config(font=('verdana',14))

button_equal = Button(root, text='=', bg='#6da9d8', fg='black', width=5, height=2, padx = 20, pady = 20, command=get_result)
button_equal.grid(row=5, column=3)
button_equal.config(font=('verdana',14))

button_div = Button(root, text='/', bg='#fff', fg='black', width=5, height=2, padx = 20, pady = 20, command=lambda :get_operator('/'))
button_div.grid(row=4, column=3)
button_div.config(font=('verdana',14))

button_square = Button(root, text='x^2', bg='#fff', fg="black", width=5, height=2, padx=20, pady=20, command=lambda :get_operator('x^2'))
button_square.grid(row=5, column=0)
button_square.config(font=('verdana',14))

button_area = Button(root, text='Area', bg='#fff', fg="black", width=5, height=2, padx=20, pady=20, command=lambda :get_operator('Area'))
button_area.grid(row=4, column=2)
button_area.config(font=('verdana',14))

button_currency_1 = Button(root, text='C/$', bg='#fff', fg="black", width=5, height=2, padx=20, pady=20, command=lambda :get_operator('C/$'))
button_currency_1.grid(row=5, column=1)
button_currency_1.config(font=('verdana',14))

button_currency_2 = Button(root, text='C/₹', bg='#fff', fg="black", width=5, height=2, padx=20, pady=20, command=lambda :get_operator('C/₹'))
button_currency_2.grid(row=5, column=2)
button_currency_2.config(font=('verdana',14))

button = tk.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
root.mainloop()