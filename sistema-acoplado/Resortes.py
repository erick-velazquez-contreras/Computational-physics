#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:27:48 2024

@author: erickvelazquez
"""

# 2. Masas y resortes.

from numpy import*
from pylab import*

# Definimos las constantes a usar. ||--k1--m1--k2--m2--k3--||

# Constantes de restitución de los resortes.
k1 = 1
k2 = 2
k3 = k1

# Masas involucradas.
m1 = 5
m2 = m1

# Posiciones iniciales de las masas.
x01 = 5
x02 = 5

# MAtriz de masas.
M = [[m1, 0],
     [0, m2]]
# Matriz de coeficientes k's.
K = [[k1+k2, -k2],
     [-k2, k2+k3]]

# De forma matricial, las ecs. de mov. se escriben:
    # Mx'' = - Kx, con x = (x1, x2).

A = dot(inv(M),K) # Matriz de la cual se necesitan los valores y vectores propios.

# Valores propios, correspondientes a las frecuencias de los modos normales.

om2, a = linalg.eig(A)
om = sqrt(om2) # Frecuencias.

N = 100 # Número de puntos a graficar.

amp = dot(linalg.inv(a), [x01, x02])  # Amplitudes direccionadas de los modos normales.

tf = 20.    # tiempo de simulación.
time = linspace(0, tf, 100)

modos = zeros((2, len(time)))

for i in range(2):
    modos[i,:] = amp[i] * cos(om[i] * time)    # modos normales.
    
Xs = dot(linalg.inv(a), modos) 

plt.figure()

plt.plot(time, Xs[0], '-g', label='Mode 1')
plt.plot(time, Xs[1], ':r', label='Mode 2')


plt.xlabel(r'$t$')
plt.ylabel(r'$x$')
plt.legend()
plt.show()
