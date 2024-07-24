import tkinter as tk

from pygame import display


def button_click_7():
    display.insert(tk.END, "7")

def button_click_8():
    display.insert(tk.END, "8")

def button_click_9():
    display.insert(tk.END, "9")

def button_click_divide():
    display.insert(tk.END, "/")

def button_click_4():
    display.insert(tk.END, "4")

def button_click_5():
    display.insert(tk.END, "5")

def button_click_6():
    display.insert(tk.END, "6")

def button_click_mutiply():
    display.insert(tk.END, "*")

def button_click_1():
    display.insert(tk.END, "1")

def button_click_2():
    display.insert(tk.END, "2")

def button_click_3():
    display.insert(tk.END, "3")

def button_click_minus():
    display.insert(tk.END, "-")

def button_click_0():
    display.insert(tk.END, "0")

def button_click_clear():
    display.delete(0, tk.END)

def button_click_equals():
    try:
        result = str(eval(display.get()))
        display.delete(0,tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error, click C to reset")

def button_click_plus():
    display.insert(tk.END, "+")

root = tk.Tk()
root.title("简易计算器")

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify=tk. RIGHT)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_7 = tk.Button(root, text="7", font=("Arial, 18"), padx=20, pady=20, command=button_click_7)
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = tk.Button(root, text="8", font=("Arial, 18"), padx=20, pady=20, command=button_click_8)
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = tk.Button(root, text="9", font=("Arial, 18"), padx=20, pady=20, command=button_click_9)
button_9.grid(row=1, column=2, padx=5, pady=5)

button_divide = tk.Button(root, text="/", font=("Arial", 18), padx=20, pady=20, command=button_click_divide)
button_divide.grid(row=1, column=3, padx=5, pady=5)

button_4 = tk.Button(root, text="4", font=("Arial, 18"), padx=20, pady=20, command=button_click_4)
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = tk.Button(root, text="5", font=("Arial, 18"), padx=20, pady=20, command=button_click_5)
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = tk.Button(root, text="6", font=("Arial, 18"), padx=20, pady=20, command=button_click_6)
button_6.grid(row=2, column=2, padx=5, pady=5)

button_mutiply = tk.Button(root, text="*", font=("Arial", 18), padx=20, pady=20, command=button_click_mutiply)
button_mutiply.grid(row=2, column=3, padx=5, pady=5)

button_1 = tk.Button(root, text="1", font=("Arial, 18"), padx=20, pady=20, command=button_click_1)
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = tk.Button(root, text="2", font=("Arial, 18"), padx=20, pady=20, command=button_click_2)
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = tk.Button(root, text="3", font=("Arial, 18"), padx=20, pady=20, command=button_click_3)
button_3.grid(row=3, column=2, padx=5, pady=5)

button_minus = tk.Button(root, text="-", font=("Arial", 18), padx=20, pady=20, command=button_click_minus)
button_minus.grid(row=3, column=3, padx=5, pady=5)

button_clear = tk.Button(root, text="C", font=("Arial", 18), padx=20, pady=20, command=button_click_clear)
button_clear.grid(row=4, column=0, padx=5, pady=5)

button_0 = tk.Button(root, text="0", font=("Arial", 18), padx=20, pady=20, command=button_click_0)
button_0.grid(row=4, column=1, padx=5, pady=5)

button_equals = tk.Button(root, text="=", font=("Arial", 18), padx=20, pady=20, command=button_click_equals)
button_equals.grid(row=4, column=2, padx=5, pady=5)

button_plus = tk.Button(root, text="+", font=("Arial", 18), padx=20, pady=20, command=button_click_plus)
button_plus.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()