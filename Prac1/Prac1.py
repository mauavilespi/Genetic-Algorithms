#Práctica 1
#Aviles Piña Mauricio
#16DIC2020

#Llamado de bibliotecas para el uso
import math #Operaciones como sen & cos
import random #Números aleatorios
import matplotlib.pyplot as plt #Gráficas
import os #Manejo cmd
import plus #Funciones a usar

#Limpiar pantalla
os.system("cls")

#Portada
plus.portada()

# Funciones fitness
print(u"Función Fitness")
print(u"1. x^2")
print(u"2. abs((x-5)/(2+sen(x)))")
print(u"3. PI*cos(PI/x)")

# Pedir al usuario que funcion Fitness quiere usar
while True:
    funcion_Fit = int(input(u"¿Qué función Fitness desea usar?"))
    if (funcion_Fit <= 3 and funcion_Fit > 0):
        break

print ("Hello World")