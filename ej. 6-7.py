# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 6 - Pràctica 7."""

def estar(cadena,caracter):
    for i in range(len(cadena)):
        if cadena[i]==caracter:
            estar=True
        else:
            estar=False
    return estar

nombre=raw_input("Escribe un nombre: ")
caracter=raw_input("Escribe un caracter: ")

v_estar=estar(nombre,caracter)

if v_estar:
    print "El caracter si esta en la cadena introducida"
else:
    print "El caracter no esta en la cadena introducida"
