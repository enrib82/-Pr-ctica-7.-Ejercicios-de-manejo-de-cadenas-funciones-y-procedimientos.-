# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 1 - Pràctica 7.
Escribe un programa que pida un texto por pantalla, este texto lo
pase como parámetro a un procedimiento, y éste lo imprima primero
 todo en minúsculas y luego todo en mayúsculas."""

texto=raw_input("Escribe un texto: ")

def definicion(pepe):
    print pepe.lower()
    print pepe.upper()
    

definicion(texto)
