# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 8 - Pràctica 7."""

def eliminar_espacios(cadena):
    sentence=""
    for i in range(len(cadena)):
        if not cadena[i]==" ":
            sentence=sentence+cadena[i]
    return sentence
frase=raw_input("Escribe una frase: ")

blanco=eliminar_espacios(frase)

print blanco
