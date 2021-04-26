import random
#Valeur par defaut des carctéristique numériques à la naissance de Tamagotchi (au démarrage du jeu)
DEFAULT_NUMERIC_VALUE = 60
#Fonction pour ne par dépasser 100% ou descendre en dessous de 0% des caractéristiques
def valeurEntreBorne(valeur):
        if valeur > 100 :
            return 100
        elif valeur < 0 :
            return 0
        else :
            return valeur

class Tamagotchi:
    #initialisations des variables
    def __init__(self):      
        self.name = ""
        self.faim = DEFAULT_NUMERIC_VALUE 
        self.soif = DEFAULT_NUMERIC_VALUE 
        self.humeur = DEFAULT_NUMERIC_VALUE 
        self.sommeil = DEFAULT_NUMERIC_VALUE 
        self.sante = DEFAULT_NUMERIC_VALUE 
        self.age = 0 
        self.sleeping = False
        #Caractéristiques calculées à partir des autres caractéristiques
        self.etat = (self.humeur + self.sante + self.faim + self.sommeil + self.soif) / 5
        self.state = "normal"

    # Impression
    def __str__(self):
        return "{"+"Nom:"+str(self.name)+'\n'+"Age:"+str(self.age)+'\n'+"Etat:"+str(self.etat)+'\n'+"Faim:"+str(self.faim)+'\n'+"Soif:"+str(self.soif)+'\n'+"Sommeil:"+str(self.sommeil)+'\n'+"Santé:"+str(self.sante)+'\n'+"Hummeur:"+str(self.humeur)+'\n'+"}"
    
    #getters
    def getName(self):
        return self.name
    
    def getFaim(self):
        return self.faim

    def getSoif(self):
        return self.soif
    
    def getHumeur(self):
        return self.humeur
    
    def getSommeil(self):
        return self.sommeil

    def getSante(self):
        return self.sante
    
    def getAge(self):
        return self.age

    def getEtat(self):
        return self.etat

    def getState(self):
        return self.state

    def isSleeping(self):
        return self.sleeping
    
    #setters
    #Fonctionnent uniquement si tamagotchi n'est pas mort
    #Le maximum des caractéristique est de 100%
    def setName(self,_name):
        self.name = _name

    def setFaim(self,_faim):
        if self.state != "mort":
            self.faim = valeurEntreBorne(_faim) 
            self.updateCalculatedCaracteristics()

    def setSoif(self, _soif):
        if self.state != "mort":
            self.soif = valeurEntreBorne(_soif)
            self.updateCalculatedCaracteristics()

    def setHumeur(self,_humeur):
        if self.state != "mort":
            self.humeur = valeurEntreBorne(_humeur)
            self.updateCalculatedCaracteristics()
    
    def setSommeil(self,_sommeil):
        if self.state != "mort":
            self.sommeil = valeurEntreBorne(_sommeil)
            self.updateCalculatedCaracteristics()

    def setSante(self, _sante):
        if self.state != "mort":
            self.sante = valeurEntreBorne(_sante) 
            self.updateCalculatedCaracteristics()

    def setAge(self, _age):
        if self.state != "mort":
            self.age = valeurEntreBorne(_age)
            self.updateCalculatedCaracteristics()
        

    def updateState(self):
        if self.age == 100 or self.faim == 0 or self.soif == 0 or self.humeur ==0 or self.sante == 0 or self.sommeil == 0 or self.etat < 15:
            self.state = "mort"
        elif self.sleeping:
            self.state = "dort"
        elif self.sante < 50:
            self.state = "malade"
        else : 
            self.state = "normal"

    def updateEtat(self):
        self.etat = (self.humeur + self.sante + self.faim + self.sommeil + self.soif) / 5
    
    def updateCalculatedCaracteristics(self):
        self.updateEtat() 
        self.updateState()

        
    # Fonction qui permet de vivre un instant de la vie, 
    # elle décrémente les caractéristiques d'un nombre aléatoire compris entre 1 et 10 
    # si tamagotchi ne dort pas le someil est aussi diminué d'un nombre aléatoir entre 1 et 10
    # si tamagotchi dort alors le sommeil est incrémenté de 15.
    # l'Age est à cahque fois incrémenté de 1
   
    def vivre(self):     
        #Generation de 5 nombres alétoires compris entre 1 et 10
        randomlist = random.sample(range(1,10), 5)

        self.setSante(self.sante - randomlist[0])
        self.setFaim(self.faim - randomlist[1])
        self.setHumeur(self.humeur - randomlist[2])
        self.setSoif(self.soif - randomlist[3])
        self.setAge(self.age + 1) 
        if not self.sleeping:
            self.setSommeil(self.sommeil - randomlist[4])      
        else:
            self.setSommeil(self.sommeil + 15)
                

    #Fonctions d'actions sur le  taagotchi, ne marchent que si tamagotchi ne dort pas
    #Si tamagotchi dort uniquement la focntion reveiller fonctionne
    def boireEau(self):
        if not self.sleeping:
            self.setSoif(self.soif+15)

    def boireCafe(self):
        if not self.sleeping:
            self.setSoif(self.soif + 5)
            self.setSommeil(self.sommeil + 10)
            self.setSante(self.sante - 5)
     
    
    def mangerGateau(self):
        if not self.sleeping:
            self.setFaim(self.faim + 15)
            self.setHumeur(self.humeur + 10)
            self.setSante(self.sante - 5)


    def mangerSalade(self):
        if not self.sleeping:
            self.setFaim(self.faim + 10)
     

    def jouer(self):
        if not self.sleeping:
            self.setHumeur(self.humeur + 10)
   
    
    def soigner(self):
        if not self.sleeping:
            self.setSante(self.sante + 20)

    def dormir(self):
        self.sleeping = True
        self.updateState()

    def reveiller(self):
        self.sleeping = False
        self.updateState()
   