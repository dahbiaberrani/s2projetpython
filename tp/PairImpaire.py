from tkinter import Button, Entry, Label, StringVar, Tk
from tkinter.constants import RIGHT


def PairImpaire():
    nb = int(nombre.get())
    if nb % 2 == 0:
       label_var.set(str (nb)+" est Pair")
    else:
        label_var.set(str (nb)+" est Impair")


my_window = Tk()
nombre = StringVar()
label_var= StringVar()
my_entry = Entry(my_window,textvariable=nombre,width=30)
my_entry.pack()

my_button = Button(my_window,text="pairImpaire",command=PairImpaire)
my_button.pack()
my_label = Label(my_window, textvariable=label_var)
my_label.pack


my_window.mainloop()

