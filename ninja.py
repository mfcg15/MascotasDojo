import mascota

class Ninja:

    def __init__(self,nombre,apellido,mascotas,premio,comida_mascota):
        self.name = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascota
    
    def caminar(self):
        self.mascotas.jugar()
        return self
    
    def alimentar(self):
        self.mascotas.comer()
        return self
    
    def bañar(self):
         self.mascotas.sonido()
         return self

mascota1 = mascota.Mascota("Mr. Nibbles","perro",["salsillas","papas"],10,5,"ladrar")
ninja1 = Ninja("Adrian","Morillo",mascota1,["snacks","galletas"],["Pizza","Burger"])
ninja1.alimentar().caminar().bañar()