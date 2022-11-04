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

print(ramasTomadas[:])


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
