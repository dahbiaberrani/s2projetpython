import random
class Tamagotchi:
    #initialisations des variables
    def __init__(self):      
        self.name = ""
        self.faim = 50
        self.soif = 50
        self.humeur = 50
        self.sommeil = 100
        self.sante = 100
        self.age = 0
        self.etat = (self.humeur + self.sante + self.faim + self.sommeil + self.soif) / 5
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
    
    #setters
    def setName(self,_name):
        self.name = _name

    def setFaim(self,_faim):
        self.faim = _faim

    def setSoif(self, _soif):
        self.soif = _soif

    def setHumeur(self,_hummeur):
        self.humeur = _hummeur
    
    def setSommeil(self,_sommeil):
        self.sommeil = _sommeil

    def setSante(self, _sante):
        self.sante = _sante

    def setAge(self, _age):
        self.age = _age

    def updateEtat(self):
        self.etat = (self.humeur + self.sante + self.faim + self.sommeil + self.soif) / 5
        
    #Mise à jour de l'Etat

    # Fonction qui permet de vivre un instant de la vie, elle décrémente les caractéristiques d'un nombre aléatoire compris entre 1 et 10
    # chaque décrémentation et indépendante de l'autre pour ne pas diminué les caractéristiques d'un même nombre
    # l'age est au contraire pas diminué aléatoirement mais augmenté de 1 
    # l'Etat est remis à jours selon est calculé à partir des autres caractéristiques
    # le nom reste inchangé
    # On permet pas d'avoir des valeur négatives, le minimum est donc 0
    # si l'une des caractéristiques est à 0 ou l'age est à 200 ans alors le tamagotchi est mort
    def vivre(self):
        #Generation de 5 nombres alétoires compris entre 1 et 10
        randomlist = random.sample(range(1, 10), 5)

        self.sante -= randomlist[0]
        if self.sante < 0:
            self.sante = 0

        self.faim -= randomlist[1]
        if self.faim < 0:
            self.faim = 0

        self.humeur -= randomlist[2]
        if self.humeur < 0:
            self.humeur = 0

        self.soif -= randomlist[3]
        if self.soif < 0:
            self.soif = 0

        self.sommeil -=randomlist[4]
        if self.sommeil < 0:
            self.sommeil = 0

        self.age += 1
        self.updateEtat()

