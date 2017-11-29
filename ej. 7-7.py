# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 7 - Pràctica 7."""

def contar(sentence):
    vocales=["A", "E", "I","O", "U", "a","e", "i", "o","u"];vocal=0
    for i in range(len(sentence)):
        for j in range(len(vocales)):
            if vocales[j]==sentence[i]:
                vocal=vocal+1
    print "La frase introducida tiene",vocal,"vocales"

frase=raw_input("Escribe una frase: ")

contar(frase)
