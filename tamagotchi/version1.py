from tkinter import *
import tkinter
from tkinter.ttk import Progressbar
import time
from threading import Thread
from tamagotchi import *
ma_fenetre = Tk()
ma_fenetre.title("Mon tamagotchi")
monTamagotchi = Tamagotchi()

difficulte = 2

def updateGuiSoif(_soif):
    soif.set(_soif)
    progress_soif['value'] = _soif

def updateGuiFaim(_faim):
    faim.set(_faim)
    progress_faim['value'] = _faim

def updateGuiHumeur(_humeur):
    humeur.set(_humeur)
    progress_humeur['value'] = _humeur

def updateGuiSommeil(_sommeil):
    sommeil.set(_sommeil)
    progress_sommeil['value'] = _sommeil

def updateGuiSante(_sante):
    sante.set(_sante)
    progress_sante['value'] = _sante

def updateGuiEtatGeneral(_etat):
    etat.set(_etat)
    progress_etat['value'] = _etat

def updateGuiAge(_age):
    age.set(_age)

def updateGui():
    updateGuiSoif(monTamagotchi.getSoif())
    updateGuiFaim(monTamagotchi.getFaim())
    updateGuiSommeil(monTamagotchi.getSommeil())
    updateGuiHumeur(monTamagotchi.getHumeur())
    updateGuiSante(monTamagotchi.getSante())
    updateGuiEtatGeneral(monTamagotchi.getEtat())
    updateGuiAge(monTamagotchi.getAge())

def runGame():
    while True:
        time.sleep(difficulte)
        monTamagotchi.vivre()
        updateGui()
        print("Un an de vie en plus")

    


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
    sommeil.set(sommeil.get()+5)
    humeur.set(humeur.get() + 5)
    sante.set(sante.get()+2)
    etat.set(( sante.get() + sommeil.get() + humeur.get() + soif.get() + faim.get()) / 5)







faim = IntVar()
soif = IntVar()
humeur = IntVar()
sommeil = IntVar()
sante = IntVar()
age = IntVar()
etat = IntVar()
nom = StringVar()
nom_choisi = StringVar()



#boutons pour interagir avec le tamagoshi

#information sur le tamagoshi
Frame_info = Frame(ma_fenetre, width=900,height=200,bd=10, bg="white")
Frame_info.grid(row=0,column=1)

info_nom = Label(Frame_info, text = "Mon nom:")
info_nom.grid(row=1,column=2)
nom_tama = Label(Frame_info, width="15", textvariable=nom)
nom_tama.grid(row=2,column=2)
nom_entry = Entry(Frame_info, textvariable= nom_choisi , font= ("Time", 20))
nom_entry.grid(row=2,column=2)
nom_button= Button(Frame_info, text="Entree", font =("Comic sans", 15), command = mon_nom )
nom_button.grid(row=3,column=2)

Frame_age = Frame(ma_fenetre, width=900,height=200,bd=10, bg="white")
Frame_age.grid(row=1,column=0)
info_age = Label(Frame_age, text = "Mon age:")
info_age.grid()
age_tama = Label(Frame_age, width="40", textvariable=age)
age_tama.grid()


can1 = Canvas(Frame_info, width =500, height =600, bg ='green')
photo = PhotoImage(file ='tamagotchi_dorme.gif')
item = can1.create_image(180, 210,  image =photo)
can1.grid(row=4,column=2) 



#statisitques, ses barres d'état en théorie
# Frame pour soif et Progress bar widget pour soif 
Frame_indicateur = Frame(ma_fenetre, width=900,height=200,bd=10, bg="white")
Frame_indicateur.grid(row=0,column=0)
group_soif = Frame(Frame_indicateur,   width=200,height=40,bd=4, bg="light grey")
group_soif.grid(row=0,column=0)
progress_soif = Progressbar(group_soif,orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_soif['value'] = soif.get()  
progress_soif.grid()

ma_soif = Label(group_soif, text = "soif: ")
ma_soif.grid()
boire = Label(group_soif,text = "soif: ", textvariable = soif)
boire.grid()



# Frame pour faim et Progress bar widget pour faim

group_faim = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
group_faim.grid()
progress_faim = Progressbar(group_faim,orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_faim['value'] = faim.get()
progress_faim.grid()

ma_faim = Label(group_faim, text = "faim: ")
ma_faim.grid()
manger = Label(group_faim, textvariable = faim)
manger.grid()


# Frame pour hummeur et Progress bar widget pour humeur
group_humeur = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
group_humeur.grid()
progress_humeur = Progressbar(group_humeur,orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_humeur['value'] = humeur.get()
progress_humeur.grid()
mon_humeur = Label(group_humeur, text = "humeur: ")
mon_humeur.grid()
jouee = Label(group_humeur, textvariable = humeur)
jouee.grid()

# Frame pour sante et Progress bar widget pour sante
group_sante = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
group_sante.grid()
progress_sante = Progressbar(group_sante,orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_sante['value'] = sante.get()
progress_sante.grid()
ma_sante = Label(group_sante, text = "santé: ")
ma_sante.grid()
soignee = Label(group_sante, textvariable = sante)
soignee.grid()

# Frame pour sommeil et Progress bar widget pour sommeil
group_sommeil = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
group_sommeil.grid()
progress_sommeil = Progressbar(group_sommeil,orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_sommeil['value'] = sante.get()
progress_sommeil.grid()
mon_sommeil = Label(group_sommeil, text = "sommeil: ")
mon_sommeil.grid()
dormiir = Label(group_sommeil, textvariable = sommeil)
dormiir.grid()

# Frame pour etat général et Progress bar widget pour etat général
group_etat = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
group_etat.grid()
progress_etat = Progressbar(group_etat,orient = HORIZONTAL,length = 100, mode = 'determinate')
progress_etat['value'] = etat.get()  
progress_etat.grid()
info_etat = Label(group_etat, text = "etat general:")
info_etat.grid()
etat_general = Label(group_etat,  textvariable=etat)
etat_general.grid()



#boutons pour interagir avec le tamagoshi
Frame_button = Frame(ma_fenetre, width=900,height=200,bd=10, bg="grey")
Frame_button.grid(row=1,column=1)
boisson = Menubutton(Frame_button, text = "Donner à boire", font =("Comic sans", 15))  
boisson.menu = Menu(boisson, tearoff = 0) 
boisson["menu"] = boisson.menu  
boisson.menu.add_command(label = "Donner de l'eau", command = boire_eau )
boisson.menu.add_command(label = "Donner du café", command = boire_cafe)
boisson.grid(row=0,column=0)

frigo = Menubutton(Frame_button, text = "Donner à manger", font =("Comic sans", 15))  
frigo.menu = Menu(frigo, tearoff = 0) 
frigo["menu"] = frigo.menu  
frigo.menu.add_command(label = "Donner un gateau", command = manger_gateau )
frigo.menu.add_command(label = "Donner une salade", command = manger_salade)
frigo.grid(row=0,column=1)

jeu = Button(Frame_button, text="Jouer", font =("Comic sans", 15), command = jouer )
jeu.grid(row=0,column=2)

pilule = Button(Frame_button, text="Donner pilule", font =("Comic sans", 15), command = soigner )
pilule.grid(row=0,column=3)

faire_dormir = Button(Frame_button,text="dormir",font =("Comic sans", 15), command = dormir)
faire_dormir.grid(row=0,column=4)
mon_label = Label(Frame_button, textvariable=dormir)
mon_label.grid(row=0,column=5)


#Thread pour executer en boucle la fonction vivre
vivreThread = Thread(target=runGame)

#initialisations de l'interface graphique
updateGui()
#lancement du jeu
vivreThread.start()
ma_fenetre.mainloop()