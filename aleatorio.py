#creamos un archivo nuevo
#guardamos en la carpeta del repositorio
#con la extension .py
#uso de numeros aleatorios

#importamos la libreria randint
from random import randint
aleatorio=randint(0,20)  #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)         #imprimimos el numero generado

#ejercicio 
#escribir una funcion sorteo() que reciba una lista de participantes, y 
# elegir a uno de los participantes aleatoriamente, y
# retornar esa persona elegida 
# desafio: no volver a retornar una persona ya sorteada


from random import randit     #importamos la funcion randint de libreria random          
def sorteo_fin_de_año(lista): #definimos una funcion          
    cant=len(lista)-1         #utilizamos lend() para saber la cantidad de personas que hay en la lista y guardamos en cant              
    indice=randint(0,cant)    #generamos un indice aleatorio 
    ganador=lista[indice]     #seleccionamos un elemento de la lista y guardamos en la variable ganador 
    return ganador            #retornamos ganador 
    print(ganador)              #esto no se ejecuta
participantes=["pau","lucas","vale","sara"] #creamos la lista de los participantes
ganar=sorteo_fin_de_año(participantes) #llamamos a la funcion y guardamos en una variable el resultado retornado por una funcion 
print(ganar)     #imprimimos el ganador 



