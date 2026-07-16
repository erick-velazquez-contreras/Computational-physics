#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:45:09 2024

@author: erickvelazquez
"""
# Solución numérica graficada.

from numpy import*
from pylab import*
import matplotlib.pyplot as plt

L = 1 # Longitud de la barra.
N = 100 # Número de puntos en los que se divide la barra.
dx = L /(N-1) # Paso espacial.

# Características del aluminio.
Ka = 50 # Conductividad termica (cal/(m s°C))
C = 0.22 # Calor especifico (cal/g°C)
p = 2700000 # Densidad (g/m^3)

k = Ka/(C*p) # Difusividad térmica.
nc = (dx**2)/(2*k) #von Neumann-Courant. Con estos datos, nc = 0.6060...
dt = 0.1 # Paso temporal. Debe ser menor a 'nc'.
h = (k*dt)/(dx**2) # Constante eta. Que no se confunda con los pasos dx o dt.

tin = 0 # Tiempo inicial.
tf = 5000 # tiempo final.

Tin = 100 # Temp inicial de la barra.

# Temperaturas en los extremos de la barra.
T_o = 0 # En x=0.
T_l = 0 # En x=L.

x = linspace(0, L, N) # Se discretiza el espacio.
tau = linspace(0, tf, int(tf/dt)) # Se discretiza el tiempo.

T = zeros((size(x), size(tau))) + Tin # Matriz de temperatura T(x,t).

# Se ponen las condiciones de forntera.
for k in range(0, size(tau), 1):
    #T[0][k] = T[size(x)-1][k] = 0
    T[size(x)-1][k] = T_l 
    T[0][k] = T_o

# Se aplica el método numérico.
for j in range(size(tau)-1):
    for i in range(1, size(x)-1):
        T[i][j+1] = T[i][j] + h*(T[i+1][j] + T[i-1][j] - 2*T[i][j])

# Proceso de graficación.

ax = plt.axes(projection="3d")

X, Y = meshgrid(tau, x)
Z = T

ax.plot_surface(X, Y, Z, cmap="plasma")

ax.set_zlim(0, 110)
ax.set_xlim(0, tf)
ax.set_ylim(0, L)
ax.set_title("Solución numérica.")
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x$')
ax.set_zlabel(r'$T(x,t)$')
ax.view_init(15,30)
plt.show()
