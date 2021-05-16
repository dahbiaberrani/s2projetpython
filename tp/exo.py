from tkinter import *

def affiche():
    
    print(categorie.get())


ma_fenetre = Tk()
categorie = StringVar()
categorie.set("Hello")
choix_Anglais = Radiobutton(ma_fenetre,text="anglais",width=20,variable=categorie,value="Hello",command=affiche)
choix_Français = Radiobutton(ma_fenetre,text="français",width=20,variable=categorie,value="Bonjour",command=affiche)
choix_Anglais.pack()
choix_Français.pack()
ma_fenetre.mainloop()