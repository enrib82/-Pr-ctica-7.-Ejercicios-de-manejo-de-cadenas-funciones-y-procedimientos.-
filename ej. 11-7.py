# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 11 - Pràctica 7."""

def palindromo(texto):
    al_reves=""
    for i in range(len(texto)-1,-1,-1):
        al_reves=al_reves+texto[i]
    return al_reves

algo=raw_input("Escribe algo: ")

reves=palindromo(algo)

if reves==algo:
    print "El resultado es",reves,": Es palindromo"
else:
    print "El resultado es",reves,": No es palindromo"
