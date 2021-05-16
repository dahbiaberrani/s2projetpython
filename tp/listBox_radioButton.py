from tkinter import *


def maj():
    l = langue.get()
    c = couleur.get()
    if l == "français" :
        salut.set("Bonjour")
        if c == "Bleu":
            hello["fg"]="Bleu"
        elif c == "Rouge":
            hello["fg"]="Rouge"
        else:
            hello["fg"]="Bleu"


        
    else:
        salut.set("Hello")

        if c == "Bleu":
            hello["fg"]="Bleu"
        elif c == "Rouge":
            hello["fg"]="Rouge"
        else:
            hello["fg"]="Bleu"


ma_fenetre = Tk()
salut = StringVar()
salut.set("Bonjour")
mon_label = Label(ma_fenetre,textvariable=salut)
mon_label.grid()


ma_liste=Listbox(ma_fenetre)
ma_liste.grid(row=0,column=3)
ma_liste.insert(END,"Bleu")
ma_liste.insert(END,"Rouge")
ma_liste.insert(END,"Vert")
  

couleur=StringVar()
couleur.set("Bleu")


langue = StringVar()
langue.set("français")
hello = Label(ma_fenetre,textvariable=salut,width=20,fg=couleur)
choix_f = Radiobutton(ma_fenetre,text = "français",width =20, variable = langue , value = "français")


choix_a = Radiobutton(ma_fenetre,text = "anglais",width =20, variable = langue , value = "anglais")

choix_f.grid()
choix_a.grid()
mon_bouton = Button(ma_fenetre,text = "activer",width=10,command = maj )
mon_bouton.grid()
ma_fenetre.mainloop()