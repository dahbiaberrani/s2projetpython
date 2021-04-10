from tkinter import *
import tkinter
from tkinter.ttk import Progressbar
import time
from threading import Thread
from tamagotchi import *
ma_fenetre = Tk()
ma_fenetre.title("Mon tamagotchi")
monTamagotchi = Tamagotchi()
#Parametres du jeux
difficulte = 10

#paramètres pour l'animation des images gif
gif_index = 0
gifRefreshIntervalTime = 50

#Différentes couleurs pour les progress bars ( vert, Orange, rouge)
#Vert
progressBarStyleVert = tkinter.ttk.Style()
progressBarStyleVert.theme_use("classic")
progressBarStyleVert.configure("green.Horizontal.TProgressbar", background='green')

#Orange
progressBarStyleVert = tkinter.ttk.Style()
progressBarStyleVert.theme_use("classic")
progressBarStyleVert.configure("orange.Horizontal.TProgressbar", background='orange')

#Rouge
progressBarStyleRouge = tkinter.ttk.Style()
progressBarStyleRouge.theme_use("classic")
progressBarStyleRouge.configure("red.Horizontal.TProgressbar", background='red')

# fonction pour changer la couleur d'une progress bar donnée en paramètre selon la valeur donnée en apramètre
def updateProgressBarColor(progressbar, value):
    if value < 25:
        progressbar.configure(style="red.Horizontal.TProgressbar")
    elif value < 50:
        progressbar.configure(style="orange.Horizontal.TProgressbar")  
    else:
        progressbar.configure(style="green.Horizontal.TProgressbar")
# foction pour mettre a jour la progress bar de l'age (les couleurs fonctionnent à l'inverse des autres bars)
# a l'etat très vieux (age > 90 ans) la couleur est rouge
# a l'etat vieux (age > 70 ans) la couleur est orange
# a l'etat jeune (age < 70 ans) la couleur est verte
def updateAgeProbressBarColor(age):
    #si age est > a 90% de l'age de la mort alors couleur rouge
    if age > 90 :
        progress_age.configure(style="red.Horizontal.TProgressbar")
    #si age est > a 70% de l'age de la mort alors couleur orange
    elif age > 70 :
        progress_age.configure(style="orange.Horizontal.TProgressbar")  
    else:
        progress_age.configure(style="green.Horizontal.TProgressbar")

#Fonctions pour la mise à jour des élements de l'interface graphique
def updateGuiSoif(_soif):
    soif.set(_soif)
    progress_soif['value'] = _soif
    updateProgressBarColor(progress_soif,_soif)

def updateGuiFaim(_faim):
    faim.set(_faim)
    progress_faim['value'] = _faim
    updateProgressBarColor(progress_faim,_faim)

def updateGuiHumeur(_humeur):
    humeur.set(_humeur)
    progress_humeur['value'] = _humeur
    updateProgressBarColor(progress_humeur,_humeur)

def updateGuiSommeil(_sommeil):
    sommeil.set(_sommeil)
    progress_sommeil['value'] = _sommeil
    updateProgressBarColor(progress_sommeil,_sommeil)

def updateGuiSante(_sante):
    sante.set(_sante)
    progress_sante['value'] = _sante
    updateProgressBarColor(progress_sante,_sante)

def updateGuiEtatGeneral(_etat):
    etat.set(_etat)
    progress_etat['value'] = _etat
    updateProgressBarColor(progress_etat,_etat)

def updateGuiAge(_age):
    age.set(_age)
    progress_age['value'] = _age
    updateAgeProbressBarColor(_age)

# focntion de mise à jour de l'image affichée selon l'activité actuelle de tamagotchi
def updateGuiImage(_state):
    # variable globale de la photo msie dans le caneva
    global photo
        
    if _state == "mort":
        photo = photo = PhotoImage(file ='./ressources/tamagotchi_mort.gif')
        can1.configure(bg='red')
    elif _state == "dort":
        photo = photo = PhotoImage(file ='./ressources/tamagotchi_dorme.gif')
        can1.configure(bg='black')
    elif _state == "malade" :
        photo = photo = PhotoImage(file ='./ressources/tamagotchi_malade.gif')
        can1.configure(bg='orange')
    else: #normal
        photo = PhotoImage(file ='./ressources/tamagotchi_normal.gif')
        can1.configure(bg='green')

    can1.itemconfigure(item , image = photo)

# desactivation de tous les boutton et activation du bouton reveiller  pour reveiller Tamagotchi
def disableActionButtons():
    #désactivation des boutons
    boisson.grid_forget()
    frigo.grid_forget()
    jeu.grid_forget()
    pilule.grid_forget()
    faire_dormir.grid_forget()
    #Activation du bouton reveiller
    faire_reveiller.grid(row=0,column=4)

# activation de tous les boutons et desactivation du bouton reveiller car tamagotchi est déjà reveillé
def enableActionButtons():
    #Activation des bouton
    boisson.grid(row=0,column=0)
    frigo.grid(row=0,column=1)
    jeu.grid(row=0,column=2)
    pilule.grid(row=0,column=3)
    faire_dormir.grid(row=0,column=4)
    #Désactivation du bouton reveiller
    faire_reveiller.grid_forget()



def updateGuiButtons(_state):
    if _state != "mort":
        if _state == "dort":
            faire_dormir.configure(text="reveiller",command = reveiller)
            disableActionButtons()       
        else:
            faire_dormir.configure(text="dormir",command = dormir)
            enableActionButtons()
    else:
        #si mort alors detruire tous les boutons d'interactions
        Frame_button.destroy()

            

def nextImageFrame():
    global gif_index
    if monTamagotchi.getState() != "mort":
        try:
            photo.configure(format="gif -index {}".format(gif_index))
            gif_index += 1
        except tkinter.TclError:
            gif_index = 0
            return nextImageFrame()
        else:
            ma_fenetre.after(gifRefreshIntervalTime, nextImageFrame)

#Fonction pour la mise à jour de tous les élements de l'interface graphique
def updateGui():
    updateGuiSoif(monTamagotchi.getSoif())
    updateGuiFaim(monTamagotchi.getFaim())
    updateGuiSommeil(monTamagotchi.getSommeil())
    updateGuiHumeur(monTamagotchi.getHumeur())
    updateGuiSante(monTamagotchi.getSante())
    updateGuiEtatGeneral(monTamagotchi.getEtat())
    updateGuiAge(monTamagotchi.getAge())
    updateGuiImage(monTamagotchi.getState())
    updateGuiButtons(monTamagotchi.getState())

#Fonctions d'action sur le tamagotchi
def mon_nom():
    nomDonne = nom_choisi.get()
    if nomDonne != "":
        monTamagotchi.setName(nomDonne)
        nom.set(monTamagotchi.getName())
        nom_entry.destroy()
        nom_button.destroy()
        lancerJeu()

def selectDifficulte():
    global difficulte
    difficulte = choixDifficulteJeu.get()

def boire_eau():
    monTamagotchi.boireEau()
    updateGui()

def boire_cafe():
    monTamagotchi.boireCafe()
    updateGui()

def manger_gateau():
    monTamagotchi.mangerGateau()
    updateGui()

def manger_salade():
    monTamagotchi.mangerSalade()
    updateGui()

def jouer():
    monTamagotchi.jouer()
    updateGui()

def soigner():
    monTamagotchi.soigner()
    updateGui()

def dormir():
    monTamagotchi.dormir()
    updateGui()

def reveiller():
    monTamagotchi.reveiller()
    updateGui()


faim = IntVar()
soif = IntVar()
humeur = IntVar()
sommeil = IntVar()
sante = IntVar()
age = IntVar()
etat = IntVar()
nom = StringVar()
nom_choisi = StringVar()





#informations et apramètres à choisir par l'utlisateur avant le lancement du jeu 

# Choix du niom du tamagotchi
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

# choix du niveau du jeu parmis les options: facile, moyen, difficile
# Frame pour le choix de la difficulté du jeu
Frame_difficulte = Frame(ma_fenetre, width=900,height=200,bd=10, bg="white")
Frame_difficulte .grid(row=0,column=0)

choixDifficulteJeu = IntVar()
R1 = Radiobutton(Frame_difficulte , text="Facile", variable=choixDifficulteJeu, value = 25,command=selectDifficulte)
R1.pack( anchor = W )

R2 = Radiobutton(Frame_difficulte , text="Moyen", variable=choixDifficulteJeu, value=10,command=selectDifficulte)
R2.select() # niveau moyen selectionner par defaut
R2.pack( anchor = W )

R3 = Radiobutton(Frame_difficulte , text="Difficile", variable=choixDifficulteJeu, value=5,command=selectDifficulte)
R3.pack( anchor = W )*

#Photo représentative de Tamagotchi
can1 = Canvas(Frame_info, width =500, height =600, bg ='green')
photo = PhotoImage(file ='./ressources/tamagotchi_welcome.gif')
item = can1.create_image(180, 210,  image =photo)
can1.grid(row=4,column=2) 

#statisitques, ses barres d'état en théorie
Frame_indicateur = Frame(ma_fenetre, width=900,height=200,bd=10, bg="white")


# Frame pour soif et Progress bar widget pour soif 
group_soif = Frame(Frame_indicateur,   width=200,height=40,bd=4, bg="light grey")
#indicateurs de la soif
ma_soif = Label(group_soif, text = "soif: ")
progress_soif = Progressbar(group_soif,orient = HORIZONTAL,length = 100, mode = 'determinate') 
boire = Label(group_soif,text = "soif: ", textvariable = soif)
#mise en page des indicateurs de la soif
ma_soif.grid(row=0,column=0)
progress_soif.grid(row=0,column=1)
boire.grid(row=0,column=2)
group_soif.grid()

# Frame pour faim et Progress bar widget pour faim
group_faim = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
#indicateurs de la faim
ma_faim = Label(group_faim, text = "faim: ")
progress_faim = Progressbar(group_faim,orient = HORIZONTAL,length = 100, mode = 'determinate')
manger = Label(group_faim, textvariable = faim)
#mise en page des indicateurs de la faim
ma_faim.grid(row=0,column=0)
progress_faim.grid(row=0,column=1)
manger.grid(row=0,column=2)
group_faim.grid()

# Frame pour hummeur et Progress bar widget pour humeur
group_humeur = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
#inducateurs de l'humeur
mon_humeur = Label(group_humeur, text = "humeur: ")
progress_humeur = Progressbar(group_humeur,orient = HORIZONTAL,length = 100, mode = 'determinate')
jouee = Label(group_humeur, textvariable = humeur)
#Mise en page des indicateurs de l'humeur
mon_humeur.grid(row=0,column=0)
progress_humeur.grid(row=0,column=1)
jouee.grid(row=0,column=2)
group_humeur.grid()

# Frame pour sante et Progress bar widget pour sante
group_sante = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
#Indicateur de la santé
ma_sante = Label(group_sante, text = "santé: ")
progress_sante = Progressbar(group_sante,orient = HORIZONTAL,length = 100, mode = 'determinate')
soignee = Label(group_sante, textvariable = sante)
#mise en page des indicateurs de al santé
ma_sante.grid(row=0,column=0)
progress_sante.grid(row=0,column=1)
soignee.grid(row=0,column=2)
group_sante.grid()

# Frame pour sommeil et Progress bar widget pour sommeil
group_sommeil = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
#indicateurs de du sommeil
mon_sommeil = Label(group_sommeil, text = "sommeil: ")
progress_sommeil = Progressbar(group_sommeil,orient = HORIZONTAL,length = 100, mode = 'determinate')
dormirLabel = Label(group_sommeil, textvariable = sommeil)
#mise en page des indicateurs du sommeil
mon_sommeil.grid(row=0,column=0)
progress_sommeil.grid(row=0,column=1)
dormirLabel.grid(row=0,column=2)
group_sommeil.grid()

# Frame pour etat général et Progress bar widget pour etat général
group_etat = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
#indicateurs de l'etat général
info_etat = Label(group_etat, text = "etat general:")
progress_etat = Progressbar(group_etat,orient = HORIZONTAL,length = 100, mode = 'determinate')
etat_general = Label(group_etat,  textvariable=etat)
#mise en page des indicateurs de l'etat général
info_etat.grid(row=0,column=0)
progress_etat.grid(row=0,column=1)
etat_general.grid(row=0,column=2)
group_etat.grid()

# Frame pour l'age
Frame_age = Frame(Frame_indicateur,   width=100,height=40,bd=4, bg="light grey")
#indicateurs de l'age
info_age = Label(Frame_age, text = "Mon age:")
progress_age = Progressbar(Frame_age,orient = HORIZONTAL,length = 100, mode = 'determinate')
age_tama = Label(Frame_age, textvariable=age)
#mise en page des indicateurs de l'age
info_age.grid(row=0,column=0)
progress_age.grid(row=0,column=1)
age_tama.grid(row=0,column=2)
Frame_age.grid()

#boutons pour interagir avec le tamagoshi
Frame_button = Frame(ma_fenetre, width=900,height=200,bd=10, bg="grey")

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

faire_reveiller = Button(Frame_button,text="reveiller",font =("Comic sans", 15), command = reveiller)



# focntions à exxecuter par le thread de vivre
def runGame():
    while True:
        time.sleep(difficulte)
        monTamagotchi.vivre()
        updateGui()
        print("Un an de vie en plus")
        if monTamagotchi.getState() == "mort":
            print("Tamagotchi mort à l'age de: ",monTamagotchi.getAge()," ans")
            return

# Focntion qui lance le jeux appelé ue fois que le joueur à donné un nom         
def lancerJeu():
    #Thread pour executer en boucle la fonction vivre
    vivreThread = Thread(target=runGame)
    #initialisations de l'interface graphique
    Frame_button.grid(row=1,column=1)
    Frame_indicateur.grid(row=0,column=0)
    Frame_difficulte.destroy()
    updateGui()
    #lancement du jeu
    vivreThread.start()

ma_fenetre.after_idle(nextImageFrame)
ma_fenetre.mainloop()