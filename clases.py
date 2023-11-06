#cuando creamos una clase, es crear nuestras propias variables, palabra reservada class

# en vez de pass puedo poner ...
#PascalCase 
# class Mascota:
#     nombre = "Bobby"
#     edad = 4
#     vacuna = True


    # nombre = ""
    # edad = 0
    # vacuna = False
#metodos o atributos especificos de python cuando tengo dos guion bajos al principio y al final, __main__: eso seria el archivo donde estamos paramos
#la llamo como una funcion a la clase
# m = Mascota()
# n = Mascota()

# n.nombre = "Puppy"
#accedemos a los datos con el operador punto:

# print(m.nombre)
# print(n.nombre)

# print(type (m).__name__)

#una instancia es un objeto de una clase

#asi puedo cargarle todos los atributos despues, o cuando lo estoy ingressandoi, podemos pasarle un metodo para hacer eso
# class Mascota:
#     def __init__(self) -> None:             #init es un metodo autoconstructor de python, es para uso interno de python, se encarga de setear todos los valores, da un valor inicial a los atributos, self es uno mismo, propio eso sinifica. o tambien le podemos poner this porque en todos los lenguajes es this
#         print(self)

# m = Mascota(m)
# print(m)

#ejemplo:
class Mascota:
    #variable de clase, no es un atributo de instancia, pasa eso si declaro una variable sin self, por ejemplo PI
    #PI = 3.14
    def __init__(self, nombre, edad, vacunado, sonido) :             
        self.nombre = nombre            #esto es la manera de crear esta variable
        self.__edad = edad
        self.vacunado = vacunado
        self.sonido = sonido
        #self.PI = 3.14

    def sonar(self):
        print(self.sonido)
    
    def presentate(self):
        print(f"Soy una mascota. me llamo {self.nombre} y tengo {self.edad} años")

    @property #asi le digo que eso es una propiedad, eso se lo llama decorador 
    def edad(self):
        return self.__edad
    @edad.setter
    def set_edad(self, value):
        if value > 0:
            self.__edad = value
    
#no es un metodo que querramos reutilizar, no tiene retorno 
#juego de variables colgando del objeto mascota_1
mascota_1 = Mascota("Bobby", 5, True, "Guaaaw")
mascota_2 = Mascota("Ppuppy", 3, False, "Miauu")
mascota_1.set_edad = -23

print(mascota_1.edad)

# print(mascota_1.nombre, mascota_1.edad, mascota_1.vacunado)
# print(mascota_2.nombre, mascota_2.edad, mascota_2.vacunado)

# mascota_1.sonar()
# mascota_2.sonar()
#print(Mascota.PI)

mascota_1.presentate()
mascota_2.presentate()

