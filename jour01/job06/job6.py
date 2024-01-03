class Animal:
    def __init__(self):
        # print("un animal vient d\'etre cree")
        self. age = 0
        self. nom =''
        pass
        
    def vieillir(self):
        self. age = self. age + 1

    def nommer(self, nom):
        self. nom = nom
        
animal = Animal()

print(animal. age)

animal. vieillir()

print(animal. age)

print(animal. nom)

animal. nommer('Luna') 

print(animal. nom)