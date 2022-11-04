from win10toast import ToastNotifier
import time
import random


participantes = []

cantRamas = int(input("Ingrese la cantidad de Ramas Principales: "))
cantParticipantes = int(input("Ingrese la cantidad de Participantes: "))
ramasPrincipales = []
for i in range(cantRamas):
    ramasPrincipales.append(i + 1)

print(ramasPrincipales[:])
residuo = (len(ramasPrincipales) % cantParticipantes)
maximo = int(len(ramasPrincipales) / cantParticipantes)
print(f"maximo: {maximo}, residuo: {residuo}")


ramasTomadas = []
for i in range(len(ramasPrincipales)):
    ramaAleatoria = random.choice(ramasPrincipales)
    while (ramaAleatoria in ramasTomadas):
        ramaAleatoria = random.choice(ramasPrincipales)
    ramasTomadas.append(ramaAleatoria)

limInf = 0
limSup = 0
print(f"Rama Sorteada: {ramasTomadas}")
splitRamas = []
splitResiduo = []
for i in range(cantParticipantes):
    limSup = limInf+maximo
    print(ramasTomadas[limInf:limSup])
    splitRamas.append(ramasTomadas[limInf:limSup])
    limInf = limSup
if (residuo != 0):
    print(ramasTomadas[limSup:limSup+residuo])
    splitResiduo.append(ramasTomadas[limSup:limSup+residuo])
print("Showing split's: ")
print(splitRamas[:])
print(splitResiduo[:])

# Reasignando residuos a las otras listas
if (residuo != 0):
    for i in range(residuo):
        rand = random.choice(splitResiduo[0])
        splitRamas[i].append(rand)
        splitResiduo[0].remove(rand)

print("Showing After Order: ")
print(splitRamas[:])
print(splitResiduo[:])

'''for i in range(1, cantParticipantes+1):
    print(f"{i}", end=" ")'''


'''adition = input("Desea agregar ramas secundarias? (y/n): ")
if adition == "y":
    cantSecundarias = int(input("Ingrese la cantidad de Ramas Secundarias: "))
    for i in range(cantSecundarias):
        valorSecundaria = input("Ingrese el valor de la rama secundaria:")
        ramasPrincipales.append(valorSecundaria)
else:
    pass'''
