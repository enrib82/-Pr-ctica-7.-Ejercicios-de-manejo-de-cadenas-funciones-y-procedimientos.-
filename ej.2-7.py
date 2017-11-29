# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 7 - Ejercicio 2 - Pràctica 7.
Escribe un programa que lea el nombre y los dos apellidos de una
persona (en tres cadenas de caracteres diferentes), los pase como
parámetros a una función, y ésta debe unirlos y devolver
una única cadena. La cadena final la imprimirá el programa por
 pantalla."""

def juntar(a,b,c):
    nombre_completo=a+" "+b+" "+c
    print nombre_completo
nom=raw_input("Escribe tu nombre: ")
apellido1=raw_input("Escribe tu primer apellido: ")
apellido2=raw_input("Escribe tu segundo apellido: ")
juntar(nom, apellido1, apellido2)
