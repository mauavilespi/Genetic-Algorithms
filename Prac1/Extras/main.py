import math
import random
import matplotlib.pyplot as plt


def portada():
    ipn = "INSITUTO POLITÉCNICO NACIONAL"
    escom = "ESCUELA SUPERIOR DE CÓMPUTO"
    tmap = "Aviles Piña Mauricio"
    ua = "Genetic Algorithms 3CM1"
    print(ipn.center(50, "*"))
    print(escom.center(50, "-"))
    print(tmap.center(50))
    print(ua.center(50) + '\n')
    print("Práctica 1".center(50))


# Portada de la práctica
portada()

# Funciones fitness
print("Función Fitness")
print("1. x^2")
print("2. abs((x-5)/(2+sen(x)))")
print("3. πcos(π/x)")

# Pedir al usuario qué función Fitness quiere usar
while True:
    funcion_Fit = int(input("¿Qué función Fitness desea usar? "))
    if (funcion_Fit <= 3 and funcion_Fit > 0):
        break

# Representación de los datos
print("Forma de representar los datos")
print("1. Binario")
print("2. Entero")
print("3. Gray")

# Pedir al usuario qué forma de representar los datos quiere usar
while True:
    representacion = int(input("¿Qué forma de representar los datos desea usar? "))
    if (representacion <= 3 and representacion > 0):
        break

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

# Conocer cuántos cromosomas se necesitarán (población inicial)
poblacion_inicial = int(input("¿Cuántos integrantes quiere para su población inicial? "))

# Generación de población (Tabla de datos aleatorios)
datos_random = []
for i in range(poblacion_inicial * bits):
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

#Dividir cromosomas
cromosoma_binario =[]
for k in range(poblacion_inicial):
    aux1=k*bits
    aux2=aux1+bits
    cromosoma_binario.append(datos_binario[aux1:aux2])

print(cromosoma_binario)

#Pasar a números enteros
cromosoma_entero = []
for t in range(poblacion_inicial):
    numero = ''
    for r in range(bits):
        numero = numero + str(cromosoma_binario[t][r])
    cromosoma_entero.append(int(numero,2))

print(cromosoma_entero)

#Evaluación de función elegida
resultados_funcion=[]
res=0
for i in range(poblacion_inicial):
    x = cromosoma_entero[i]
    if (funcion_Fit==1):
        res = x**2
    elif (funcion_Fit==2):
        res = abs((x-5)/(2+math.sin(x)))
    elif (funcion_Fit==3):
        res = math.pi * math.cos(math.pi / x)
    resultados_funcion.append(res)

print (resultados_funcion)

#Graficar histograma
plt.plot(resultados_funcion, 'C3')
plt.show()