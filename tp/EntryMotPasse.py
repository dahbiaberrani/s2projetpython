from tkinter import*
#  
def devoiler():
   
   mots_passe_clair.set(mots_passe.get())
   mots_passe.set("")



ma_fenetre = Tk()

mots_passe = StringVar()
my_champ = Entry(ma_fenetre,textvariable = mots_passe,show='*')
my_champ.grid(row=0,column=0)



boton_effacer = Button(ma_fenetre,text="dévoilé",command=devoiler)
boton_effacer.grid(row=0,column=1)
mots_passe_clair = StringVar()
mon_label = Label(ma_fenetre,textvariable=mots_passe_clair)
mon_label.grid(row=1,column=0)
ma_fenetre.mainloop()