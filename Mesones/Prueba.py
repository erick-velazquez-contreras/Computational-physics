#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:22:34 2024

@author: erickvelazquez
"""

# Tarea 7. 1.
# Prueba de Chi cuadrada.

from random import*
from numpy import*

n = 51 # Número de datos a tomar (números pseudoaleatorios).
k = 10 #n/5  # Número de subintervalos a tomar dentro de la distribución (0,1).

a = random.random(n) # Arreglo de n números pseudoaleatorios en (0,1).

p = 1/k # Probabilidad de encontrar un número de a en uno de sus k intervalos.

V = 0 # Sumador para hacer Chi^2.

for i in range(1, n):
    V = ((a[i] - n*p)**2)/(n*p) # Se computa la sumatoria.

#print('Probabilidad usada: ', round(p*100, 2), '%')
print('Valor de V: ', V)
print(round(n*p,2)) # Debería cumplirse que n*p >= 5., por la "regla del pulgar".

# Para n = 50, V es mucho menor a los mostrados en la tabla 1 de la sección 3.3.1 de 
# "The Art of Computer Programming - Volume 2 -Seminumerical Algorithms".
# En general, he visto que los valores de V son demasiado pequeños en comparación a los
# encontrados en tablas de valores críticos de la distribución Chi^2, por lo que no podemos asegurar
# que los números usados sean aleatorios.