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

# Info esencial
# Genes: individuos representados como un conjunto de parámetros
# Cromosomas: string donde se agrupan los genes
# Alfabeto = {0,1}
# Fenotipo: conjunto de parámetros representando un cromosoma particular
# Genotipo: información requerida para construir un organismo

# Funciones fitness
print("Función Fitness")
print("1. x^2")
print("2. ABS|(x-5)/(2+sen(x))|")
print("3. π*cos(π/x) \n")

# Elección de la función fitness
while True:
    funcion_Fit = int(input("¿Qué función Fitness desea usar? "))
    if (funcion_Fit <= 3 and funcion_Fit > 0):
        break

# Tipo de algoritmo genético
print("\nTipo de algoritmo genético")
print("1. Modelo Generacional")
print("2. Modelo Estacionario o Elitista")
print("3. Información\n")

while True:
    ag_tipo = int(input("¿Qué tipo de algoritmo genético desea usar? "))
    
    #Modelo Generacional
    if (ag_tipo == 1):
        mg_generaciones = int(input("\nIntroduzca el número de generaciones que desea: "))
         
    #Información
    if (ag_tipo == 3):
        print ("Información".center(50,'*'))
        print("Modelo Generacional: ")
        print("Durante cada iteración se crea una población completa con nuevos individuos\n")
        print("Modelo Estacionario o Elitista: ")
        print("Durante cada iteración se escogen dos padres y a estos se le aplican los operadores\n")
        break
    
    if (ag_tipo <= 2 and ag_tipo > 0):1
        break

# Especificación del rango de la población inicial

# Rango de los datos
print("Rango de los datos [A,B]")
rango_A = int(input("A: "))
rango_B = int(input("B: "))
print("Rango del usuario [" + str(rango_A) + "," + str(rango_B) + "]")

# Cantidad de bits a usar
bits = math.floor(math.log2(rango_B))+1
print("Cantidad de bits a usar: " + str(bits))
print("Para no desperdiciar números: ")
print("Nuevo Rango = [1," + str((2 ** bits) - 1) + "]")


ag_tamaño = int(input("Tamaño de población: "))