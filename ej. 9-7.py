# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio  - Pràctica 7."""

def coincidir(word1,word2):
    text1="";text2="";probado = False;contador = -1

    while not probado:
        if word1[contador] == word2[contador] and contador >= -3:
            text1=word1[contador]
            text2=word2[contador]
            contador=contador-1
        else:
            probado=True

    contador = contador+1

    if contador == -1:
        print "La ultima letra coincide"
    elif contador == -2:
        print "Las dos ultimas letras coinciden"
    elif contador == -3:
        print "Las tres ultimas letras coinciden"
    else:
        print "No coincide ninguna letra de las tres ultimas"
palabra1=raw_input("Escribe una primera palabra: ")
palabra2=raw_input("Escribe una segunda palabra: ")

while len(palabra1)<=3:
    print "Escribe la primera palabra con longitud mayor a 3:",
    palabra1=raw_input()
    while len(palabra2)<=3:
        print "Escribe la segunda palabra con longitud mayor a 3:",
        palabra2=raw_input()

coincidir(palabra1,palabra2)
