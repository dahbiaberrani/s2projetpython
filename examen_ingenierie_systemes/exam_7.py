
"""
BERRANI Dahbia
Une fenêtre est affichée avec un label represeantant l'heure actuelle lorsque on appui sur le boutton Actualiser
L'heure est affichée au format hh:mm:ss
L'action possible de l'utilisateur est d'actualisé l'heure affichée sur la fenêtre, 
la réponse à cette action est de mettre à jour l'heure de la fenêtre à l'heure ectuelle
"""
from tkinter import *
from datetime import datetime,timedelta

compteur  =0

def actualiser():
    # Récupère la date actuelle
    date = datetime.now()
    # Transforme la date en texte de la forme HH:MM:SS
    texte = f'{date.hour}:{date.minute:02d}:{date.second:02d}' # %H = heure, %M = minutes, %S = secondes
    texte_var.set(texte)


def actualiser_auto():
    actualiser()
    label.after(200, actualiser_auto)

def demarrer():
    global compteur
    datenow = datetime.now()
    delta = (compteur - datenow).total_seconds()
    min = int(delta / 60)
    sec = int( delta - (min * 60))
    # Transforme la date en texte de la forme HH:MM:SS
    texte2 = str(min)+":"+str(sec)
    texte_var2.set(texte2)
    label2.after(500, demarrer)


def reset():
    # initialisation du compteur a 15 minutes
    global compteur
    datenow = datetime.now()
    compteur = datenow + timedelta(minutes = 1)
    delta = (compteur - datenow).total_seconds()
    min = int( delta / 60)
    sec = int(delta - (min * 60))
    # Transforme la date en texte de la forme HH:MM:SS
    texte2 = str(min)+":"+str(sec)
    texte_var2.set(texte2)

# Création de la fenêtre et des widgets
ma_fenetre = Tk()

bouton = Button(
    ma_fenetre,
    text="Actualiser",
    command=actualiser
)
texte_var = StringVar()
label = Label(
    ma_fenetre,
    textvariable=texte_var
)

texte_var2 = StringVar()
label2 = Label(
    ma_fenetre,
    textvariable=texte_var2
)



bouton2 = Button(
    ma_fenetre,
    text="Reinitialiser",
    command=reset
)

reset()
# Compte à rebour actualisé chaque 500ms (1/2 second)
label2.after(500, demarrer)

# Lancer la fonction actualiser_auto dans 200ms
label.after(200, actualiser_auto)

# Placement des widgets dans la fenêtre
label.grid(row=0, column=0, padx=10, pady=10)
bouton.grid(row=0, column=1, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
bouton2.grid(row=1, column=1, padx=10, pady=10)

# Lancement de l'affichage
ma_fenetre.mainloop()
