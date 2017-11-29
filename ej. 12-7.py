# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 12 - Pràctica 7."""

def palabra(frase):
    contador=1
    for i in range(len(frase)):
        if frase[i]==" " or frase[i]=="." or frase[i]=="_" or frase[i]=="-":
            if not frase[i-1]==" " or frase[i-1]=="." or frase[i-1]=="_" or frase[i-1]=="-":
                contador=contador+1
    return contador

frase=raw_input("Escribe una frase: ")

cuenta=palabra(frase)

if cuenta>1:
    print "La frase tiene",cuenta,"palabras"
else:
    print "La frase tiene sOlo una palabra"
