from tkinter import *


def maj():
    l = langue.get()
    if l == "français" :
        salut.set("Bonjour")
        
    else:
        salut.set("Hello")




ma_fenetre = Tk()
salut = StringVar()
salut.set("Bonjour")
mon_label = Label(ma_fenetre,textvariable=salut)
mon_label.grid()




langue = StringVar()
langue.set("français")

choix_f = Radiobutton(ma_fenetre,text = "français",width =20, variable = langue , value = "français")

choix_couleur =Radiobutton(ma_fenetre,text ="r")

choix_a = Radiobutton(ma_fenetre,text = "anglais",width =20, variable = langue , value = "anglais")

choix_f.grid()
choix_a.grid()
mon_bouton = Button(ma_fenetre,text = "activer",width=10,command = maj )
mon_bouton.grid()
ma_fenetre.mainloop()