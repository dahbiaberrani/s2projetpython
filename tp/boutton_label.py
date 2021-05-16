
from tkinter import*

def compte():
    inter = int(nombre.get())+1
    nombre.set(str(inter))

ma_fenetre_2 = Tk()
nombre = StringVar()
nombre.set(str(0))
mon_label = Label(ma_fenetre_2,textvariable=nombre)
mon_label.pack()
mon_bouton = Button(ma_fenetre_2,text="ajouter 1", command=compte)
mon_bouton.pack()
ma_fenetre_2.mainloop()