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
print("3. π*x*cos(π) \n")

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
    
    if (ag_tipo <= 2 and ag_tipo > 0):
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

#Tamaño de población
ag_tamaño = int(input("Tamaño de población: "))

#Elección del tipo de representación
print("\nTipo de representación de la población: ")
print("1. Binarios")
print("2. Gray")

while True:
    ag_representacion = int(input("¿Qué tipo de representación de la población desea usar? "))

    if (ag_representacion == 1 or ag_representacion == 1):
        break

if(ag_representacion==1):
    # Generación de población (Tabla de datos aleatorios)
    datos_random = []
    for i in range(ag_tamaño * bits):
        datos_random.append(random.random())
    print(datos_random)

    # Datos en binario
    datos_binario = []
    for x in range(0, len(datos_random)):
        if (datos_random[x] >= 0.5):
            datos_binario.append(1)
        else:
            datos_binario.append(0)
    print(datos_binario)
    print('\n')

    #Dividir cromosomas
    cromosoma_binario =[]
    for k in range(ag_tamaño):
        aux1=k*bits
        aux2=aux1+bits
        cromosoma_binario.append(datos_binario[aux1:aux2])

    print(cromosoma_binario)
    print('\n')

    #Pasar a números enteros
    cromosoma_entero = []
    for t in range(ag_tamaño):
        numero = ''
        for r in range(bits):
            numero = numero + str(cromosoma_binario[t][r])
        cromosoma_entero.append(int(numero,2))

    print(cromosoma_entero)
    print('\n')

    #Evaluación de función elegida
    resultados_funcion=[]
    res=0
    for i in range(ag_tamaño):
        x = cromosoma_entero[i]
        if (funcion_Fit==1):
            res = x**2
        elif (funcion_Fit==2):
            res = abs((x-5)/(2+math.sin(x)))
        elif (funcion_Fit==3):
            res = math.pi * x * math.cos(math.pi)
        resultados_funcion.append(res)

    print (resultados_funcion)
    print('\n')

    #Min y Max
    ag_max = max(resultados_funcion)
    ag_maxpos = resultados_funcion.index(ag_max)
    ag_min = min(resultados_funcion)
    ag_minpos = resultados_funcion.index(ag_min)

    print("MAX: "+str(ag_max)+"\n")
    print("MIN: "+str(ag_min)+"\n")


    #Graficar histograma
    plt.plot(resultados_funcion, 'C3')
    plt.annotate('MAX = '+str(ag_max), xy=(ag_maxpos, ag_max), xytext=(ag_maxpos, ag_max+100),
            arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('MIN = '+str(ag_min), xy=(ag_minpos, ag_min), xytext=(ag_minpos, ag_min-100),
            arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()    
