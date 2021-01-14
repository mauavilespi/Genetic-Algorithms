#Práctica 1
#Aviles Piña Mauricio
#16DIC2020

#Python 3.7.8 64-bit
#Windows 10 

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
print("Función Fitness")
print("1. x^2")
print("2. ABS|(x-5)/(2+sen(x))|")
print("3. π*cos(π/x)")

# Pedir al usuario que funcion Fitness quiere usar
while True:
    funcion_Fit = int(input("¿Qué función Fitness desea usar? "))
    if (funcion_Fit <= 3 and funcion_Fit > 0):
        break

print ("Hello World")