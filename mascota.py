class Mascota:

    def __init__(self,nombre,tipo,golosionas,salud,energia,ruido):
        self.nombre = nombre
        self.tipo = tipo 
        self.golosinas = golosionas
        self.salud = salud
        self.energia = energia 
        self.ruido = ruido

    def dormir(self):
        self.energia += 25 
    
    def comer(self):
        self.energia += 5 
        self.salud += 10

    def jugar(self):
        self.salud +=5
    
    def sonido(self):
        print(self.nombre+" puede "+self.ruido)





