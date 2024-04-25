from tkinter import *

root = Tk()
root.title('Temperature Converter')
root.geometry()
root.config(bg='plum')
root.resizable(False, False)

my_frame = Frame(root, background='plum')
my_frame.pack(padx=5, pady=5)

Options = ["Fahrenheit", "Celsius", "Kelvin"]

temp1 = Entry(my_frame, font=("Helvetica", 19), width=10, justify=CENTER)
temp1.grid(row=0, column=0, padx=5, pady=5)

clicked1 = StringVar()
clicked1.set("Celsius")
drop1 = OptionMenu(my_frame, clicked1, *Options)
drop1.config(font=("Helvetica", 15), bg="lightblue", width=10)
drop1.grid(row=0, column=1, padx=5, pady=5)

temp2 = Label(my_frame, font=("Helvetica", 19), width=9, text="--------")
temp2.grid(row=1, column=0, padx=5, pady=5)

clicked2 = StringVar()
clicked2.set("Fahrenheit")
drop2 = OptionMenu(my_frame, clicked2, *Options)
drop2.config(font=("Helvetica", 15), bg="lightblue", width=10)
drop2.grid(row=1, column=1, padx=5, pady=5)

temp3 = Label(my_frame, font=("Helvetica", 19), width=9, text="--------")
temp3.grid(row=2, column=0, padx=5, pady=5)

clicked3 = StringVar()
clicked3.set("Kelvin")
drop3 = OptionMenu(my_frame, clicked3, *Options)
drop3.config(font=("Helvetica", 15), bg="lightblue", width=10)
drop3.grid(row=2, column=1, padx=5, pady=5)


def convert():
    f = clicked1.get()
    t = clicked2.get()
    v = clicked3.get()
    ini = int(temp1.get())
    if f == t == v:
        temp2.config(text=ini)
        temp3.config(text=ini)
        return
    if f == "Celsius":
        if t == "Fahrenheit":
            if v == "Kelvin":
                ans = round((ini * (9 / 5)) + 32, 2)
                temp2.config(text=ans)
                temp3.config(text=ans + 273.15)
            else:
                ans = round((ini * (9 / 5)) + 32, 2)
                temp2.config(text=ans)
                temp3.config(text=ans)
        elif t == "Kelvin":
            ans = round(ini + 273.15, 2)
            temp2.config(text=ans)
            temp3.config(text=ans)
    elif f == "Fahrenheit":
        if t == "Celsius":
            if v == "Kelvin":
                ans = round((ini - 32) * (5 / 9), 2)
                temp2.config(text=ans)
                temp3.config(text=ans + 273.15)
            else:
                ans = round((ini - 32) * (5 / 9), 2)
                temp2.config(text=ans)
                temp3.config(text=ans)
        elif t == "Kelvin":
            ans = round((ini - 32) * (5 / 9) + 273.15, 2)
            temp2.config(text=ans)
            temp3.config(text=ans)
    else:  # Fahrenheit
        if t == "Celsius":
            ans = round((ini - 273.15) * (9 / 5), 2)
            temp2.config(text=ans)
            temp3.config(text=ini)
        else:  # Kelvin
            ans = round(ini - 273.15, 2)
            temp2.config(text=ans)
            temp3.config(text=ans)


button = Button(root, text="Convert", command=convert, font=("Helvetica", 15),
                bg="lavender", fg="purple", activebackground="purple", activeforeground="plum"
                )
button.pack(padx=20, pady=30)

root.mainloop()
