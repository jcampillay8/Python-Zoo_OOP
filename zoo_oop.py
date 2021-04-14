class Animal:

    def __init__(self, nombre, edad, salud, felicidad):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
        
    def display_info(self):
        return "Nombre: "+self.nombre + " \nEdad: " + str(self.edad)+" \nSalud: "+str(self.salud)+" \nFelicidad: "+str(self.felicidad)

    def alimentacion(self):
        self.salud += 10
        self.felicidad +=10

class Jirafa(Animal):

    def __init__(self, altura, nombre_jirafa, edad_jirafa, salud_jirafa, felicidad_jirafa):
        super().__init__(nombre_jirafa, edad_jirafa, salud_jirafa, felicidad_jirafa)
        self.altura = altura
    
    def display_info(self):
        return super().display_info()+" \nAltura: "+str(self.altura)

    def alimentacion(self):
        return super().alimentacion()

class Elefante(Animal):

    def __init__(self, peso, nombre_elefante, edad_elefante, salud_elefante, felicidad_elefante):
        super().__init__(nombre_elefante, edad_elefante, salud_elefante, felicidad_elefante)
        self.peso = peso
    
    def display_info(self):
        return super().display_info()+" \nPeso: "+str(self.peso)

class Leon(Animal):

    def __init__(self, velocidad, nombre_leon, edad_leon, salud_leon, felicidad_leon):
        super().__init__(nombre_leon, edad_leon, salud_leon, felicidad_leon)
        self.velocidad = velocidad
    
    def display_info(self):
        return super().display_info()+" \nVelocidad: "+str(self.velocidad)

jirafa=Jirafa(6,"Jirafa",5,100,100)
elefante = Elefante(6000, "Elefante", 10,100,100 )
leon = Leon(80, "León", 4,100,100)

# print(jirafa.display_info())
# print("")
# print(elefante.display_info())
# print("")
# print(leon.display_info())

respuesta =None
eleccion=None
# while True:
    
while respuesta not in ("s","n"):
    respuesta = (input("Desea alimentar algun animal en el Zoo (s/n): ")).lower()

    if respuesta == "s":
        
        eleccion = (input("Elija si quiere alimentar a la jirafa, elefante o al león: (j, e, l) "))
        
        if eleccion == "j":

            jirafa.alimentacion()
            print(jirafa.display_info())

        if eleccion == "e":

            elefante.alimentacion()
            print(elefante.display_info()) 

        if eleccion == "l":

            leon.alimentacion()
            print(leon.display_info()) 
        
        respuesta = None

    if respuesta == "n":
        print("Gracias por venir al Zoo, tenga un buen día")
        break
    

