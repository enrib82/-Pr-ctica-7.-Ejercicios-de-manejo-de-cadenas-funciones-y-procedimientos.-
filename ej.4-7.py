# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 4 - Pràctica 7.
Escribe un programa que pida una frase, y le pase como parámetro a una
función dicha frase. La función debe sustituir todos los espacios
en blanco de una frase por un asterisco, y devolver el resultado
para que el programa principal la imprima por pantalla. """


def sustituto(cadena):
    nada=""
    for i in range(len(cadena)):
        if cadena[i]==" ":
            nada=nada+"*"
        else:
            nada=nada+cadena[i]
    return nada

frase=raw_input("Escribe una frase: ")

asteriscos=sustituto(frase)

print asteriscos
