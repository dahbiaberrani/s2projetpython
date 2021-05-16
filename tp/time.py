from tkinter import*
import time 
def affiche_heure():
    heure = time.localtime()
    print("il est ",heure[3],"heure" ,heure[4],"minute",heure[5],"seconde")
ma_fenetre = Tk()
mon_bouton = Button(ma_fenetre,text ="quelle heure est-il?",command=affiche_heure,padx=20,pady=20,font =("helvetica",20))
mon_bouton.pack()
ma_fenetre.mainloop()







