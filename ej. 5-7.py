# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 5 - Pràctica 7."""


def modificar(cadena,letra):
    text=""
    for i in range(len(cadena)):
        if cadena[i]=="a" or cadena[i]=="e" or cadena[i]=="i" or cadena[i]=="o" or cadena[i]=="u":
            text=text+letra
        else:
            text=text+cadena[i]
    return text

frase=raw_input("Escribe una frase: ")
vocal=raw_input("Escribe una vocal: ")

while len(vocal)!=1:
    vocal=raw_input("Solo una vocal, por favor: ")

cadena_modificada=modificar(frase,vocal)

print cadena_modificada
