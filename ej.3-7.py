# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 3 - Pràctica 7.
Escribe un programa que lea una frase, y la pase como parámetro a
 un procedimiento, y éste debe mostrar la frase con un carácter
 en cada línea. """

frase=raw_input("Dime una frase: ")

def funcion(g):
    for i in frase:
        print i

funcion(frase)
