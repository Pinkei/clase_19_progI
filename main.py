import os

dir_actual = os.getcwd()

print(os.path.join(dir_actual))
print(dir_actual)


lista =[]
lista_procesada = []
lista_procesada_2 = []
personas = []

with open (os.path.join(dir_actual, "personas.csv"), "r", encoding="utf-8") as file:
    file.readline() 
    lineas = file.readlines() 
#esta es una manera mas corta:
lista = [linea.strip() for linea in lineas]
lista = [linea.split(",") for linea in lineas]

# for linea in lineas[:]:
#     lista_procesada.append(linea.strip()) #para sacarle

    #split devuelve una lista con los distintos strings mas pequeños que fueron cortados

# for linea in lista_procesada:
#     lista_procesada_2.append(linea.split())

# for linea in lineas:
#     lista_procesada.append(linea.strip())
# print(lista_procesada)


# for linea in lista_procesada:
#     lista_procesada_2.append(linea.split(","))
# print(lista_procesada_2)


for persona in lista:
    dict_persona = {}
    dict_persona['id'] = int(persona[0])
    dict_persona['nombre'] = persona[1]
    dict_persona['apellido'] = persona[2]
    dict_persona['edad'] = int(persona[3])
    personas.append(dict_persona)
# print("---------------------------------")
# print(personas)

with open(os.path.join(dir_actual, "personas2.csv"), "w") as file:
    primer_persona = personas[0]
    # metodo keys me trae ?¿?¿?¿?¿?
    keys = primer_persona.keys()
    encabezado = ",".join(keys)        #elemento join separa el caracter
    file.write(encabezado + "\n")

    for persona in personas:
        values = list(persona.values())

        for index, value in enumerate(values):  #enumerate me devuelve una lista de tuplas y el valor
            
            if isinstance(value, int):
                values[index] = str(value)


        data = ",".join(values)
        data = data.upper()
        file.write(data +"\n")





