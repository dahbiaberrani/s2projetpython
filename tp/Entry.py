from tkinter import*
def effacer():
    ma_variable.set('')
def afficher():
    print(ma_variable.get())

ma_fenetre = Tk()
ma_variable = StringVar()
my_champ = Entry(ma_fenetre,textvariable =ma_variable,width=50)
my_champ.pack()
boton_effacer = Button(ma_fenetre,text="effacer",command=effacer)
boton_effacer.pack()
boton_afficher = Button(ma_fenetre,text="afficher",command=afficher)
boton_afficher.pack()
ma_fenetre.mainloop()