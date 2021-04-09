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
        self.etat = "normal"

    #getters
    def getName(self):
        return self.name
    
    def getFaim(self):
        return self.faim
    
    def getHummeur(self):
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

    def setHummeur(self,_hummeur):
        self.humeur = _hummeur
    
    def setSommeil(self,_sommeil):
        self.sommeil = _sommeil

    def setSante(self, _sante):
        self.sante = _sante

    def setAge(self, _age):
        self.age = _age

    def setEtat(self, _etat):
        self.etat = _etat
