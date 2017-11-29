# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 10 - Pràctica 7."""

def capicua(texto):
    al_reves=""
    for i in range(len(texto)-1,-1,-1):
        al_reves=al_reves+texto[i]

    if al_reves==texto:
        print algo,"es capicua o palindromo"
    else:
        print algo," no es capicua o palindromo"

    return al_reves

algo=raw_input("Escribe algo: ")

reves=capicua(algo)

print "El resultado es",reves
