#creamos un archivo nuevo
#guardamos en la carpeta del repositorio
#con la extension .py
#uso de numeros aleatorios

#importamos la libreria randint
from random import randint
aleatorio=randint(0,20)  #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)         #imprimimos el numero generado

#ejercicio 
#escribir una funcion sorteo() que reciba una lista de participantes, y s
# elegir a uno de los participantes aleatoriamente, y
# retornar esa persona elegida 
# desafio: no volver a retornar una persona ya sorteada


from random import randit
def sorteo(lista):
    aleatorio=randint(0,4)
    return lista
participantes=["pau","lucas","vale","sara"]
sorteo(participantes)

