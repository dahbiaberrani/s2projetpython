from tkinter import *
from tkinter.ttk import Progressbar
import time
from threading import Thread


ma_fenetre = Tk()
ma_fenetre.title("Mon tamagotchi")

def vivre():
    while True:
        soif.set(soif.get() - 3)
        progress_soif['value'] = soif.get()
        print("1 an de vie en plus")
        time.sleep(5)


def mon_nom():
    nom.set(nom_choisi.get())
    nom_entry.grid_forget()
    nom_button.grid_forget()

def boire_eau():
    soif.set(soif.get() + 15)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)

def boire_cafe():
    soif.set(soif.get() + 5)
    sommeil.set(sommeil.get() + 10)
    sante.set(sante.get() - 5)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)

def manger_gateau():
    faim.set(faim.get() + 10)
    humeur.set(humeur.get() + 10)
    sante.set(sante.get() - 5)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)

def manger_salade():
    faim.set(faim.get() + 15)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)

def jouer():
    humeur.set(humeur.get() + 10)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)

def soigner():
    sante.set(sante.get() + 20)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)

def dormir():
    var = compteur.get()
    if var < 15 :
        dormir.set("faire_dormir")
    else:
        dormir.set("reveiller")
















#initialisations des variables

faim = IntVar()
faim.set(50)
soif = IntVar()
soif.set(50)
humeur = IntVar()
humeur.set(50)
sommeil = IntVar()
sommeil.set(100)
sante = IntVar()
sante.set(100)
age = IntVar()
age.set(0)
etat = IntVar()
etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)
nom = StringVar()
nom_choisi = StringVar()
dormir = StringVar()
dormir.set("faire_dormir")

# Progress bar widget
progress_soif = Progressbar(ma_fenetre, orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_soif['value'] = soif.get()
  
progress_soif.grid()

#information sur le tamagoshi

info_nom = Label(ma_fenetre, text = "Mon nom:")
info_nom.grid()
nom_tama = Label(ma_fenetre, width="40", textvariable=nom)
nom_tama.grid(row=1,column=1)

info_age = Label(ma_fenetre, text = "Mon age:")
info_age.grid()
age_tama = Label(ma_fenetre, width="40", textvariable=age)
age_tama.grid()

info_etat = Label(ma_fenetre, text = "etat general:")
info_etat.grid()
etat_general = Label(ma_fenetre, width="40", textvariable=etat)
etat_general.grid()

#creation nom

nom_entry = Entry(ma_fenetre, textvariable= nom_choisi , font= ("Time", 20))
nom_entry.grid()
nom_button= Button(ma_fenetre, text="Valider", font =("Comic sans", 20), command = mon_nom )
nom_button.grid()

#statisitques, ses barres d'état en théorie

ma_soif = Label(ma_fenetre, text = "soif: ")
ma_soif.grid()
boire = Label(ma_fenetre, textvariable = soif)
boire.grid()

ma_faim = Label(ma_fenetre, text = "faim: ")
ma_faim.grid()
manger = Label(ma_fenetre, textvariable = faim)
manger.grid()

mon_humeur = Label(ma_fenetre, text = "humeur: ")
mon_humeur.grid()
jouer_ = Label(ma_fenetre, textvariable = humeur)
jouer_.grid()

ma_sante = Label(ma_fenetre, text = "santé: ")
ma_sante.grid()
soigner_ = Label(ma_fenetre, textvariable = sante)
soigner_.grid()

mon_sommeil = Label(ma_fenetre, text = "sommeil: ")
mon_sommeil.grid(row=6,column=0)
dormir_ = Label(ma_fenetre, textvariable = sommeil)
dormir_.grid()

#boutons pour interagir avec le tamagoshi
can1 = Canvas(ma_fenetre, width =700, height =500, bg ='white')
photo = PhotoImage(file ='tamagotchi_normal.gif')
item = can1.create_image(80, 80, image =photo)
can1.grid() 
boisson = Menubutton(ma_fenetre, text = "Donner à boire", font =("Comic sans", 15))  
boisson.menu = Menu(boisson, tearoff = 0) 
boisson["menu"] = boisson.menu  
boisson.menu.add_command(label = "Donner de l'eau", command = boire_eau )
boisson.menu.add_command(label = "Donner du café", command = boire_cafe)
boisson.grid()

frigo = Menubutton(ma_fenetre, text = "Donner à manger", font =("Comic sans", 15))  
frigo.menu = Menu(frigo, tearoff = 0) 
frigo["menu"] = frigo.menu  
frigo.menu.add_command(label = "Donner un gateau", command = manger_gateau )
frigo.menu.add_command(label = "Donner une salade", command = manger_salade)
frigo.grid()

jeu = Button(ma_fenetre, text="Jouer", font =("Comic sans", 15), command = jouer )
jeu.grid()

pilule = Button(ma_fenetre, text="Donner pilule", font =("Comic sans", 15), command = soigner )
pilule.grid()

mon_label = Label(ma_fenetre, textvariable=dormir)
mon_label.grid()
compteur = StringVar()
compteur.set(15)
choix_d = Radiobutton(ma_fenetre,text = "faire_dormir",width =20, variable = compteur , value = "faire_dormir")
choix_d.grid()
choix_r = Radiobutton(ma_fenetre,text = "reveiller",width =20, variable = compteur , value = "reveiller")
choix_r.grid()
mon_bouton = Button(ma_fenetre,text = "activer", width=10, font =("Comic sans", 15), command = sommeil )
mon_bouton.grid()


# create thread to simulate life

th = Thread(target=vivre)

th.start()
ma_fenetre.mainloop()