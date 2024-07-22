class Personas:
    def __init__(self, nombre, edad, numero, correo, genero, semestre):
        self.nombre = nombre
        self.edad = edad
        self.numero = numero
        self.correo = correo
        self.genero = genero
        self.semestre = semestre

nombre = input("¿Cual es su nombre? ")
edad_int = input("¿Cual es su edad? ")
numero = input("¿Cual es su numero? ")
correo = input("¿Cual es su correo? ")
genero = input("¿Cual es su genero? ")
semestre_int = input("¿En que semestre esta actualmente? ")

def mayor_menor(edad_int, nombre):
    edad = int(edad_int)
    if edad >= 18:
        print(f"{nombre} de {edad} años es mayor de edad")
    else:
        print(f"{nombre} de {edad} años es menor de edad")

def terminar_carrera(semestre):
    semestre = int(semestre)
    semestres_faltantes = 10 - semestre
    print(f"Le faltan {semestres_faltantes} semestres para terminar la carrera")
    return semestres_faltantes

mayor_menor(edad_int, nombre)
semestres_restantes = terminar_carrera(semestre_int)