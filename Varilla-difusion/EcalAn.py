#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:10:21 2024

@author: erickvelazquez
"""
# Gráfica de la solución analítica.

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

k=Ka/(C*p) # Difusividad térmica.
nc = (dx**2)/(2*k) #von Neumann-Courant. Con estos datos, nc = 0.6060...
dt = 0.1 # Paso temporal. Debe ser menor a 'nc'.
h = (k*dt)/(dx**2) # Constante eta. Que no se confunda con los pasos dx o dt.

tin = 0 # Tiempo inicial.
tf = 4000 # tiempo final.

Tin = 100 # Temp inicial de la barra.

# Temperaturas en los extremos de la barra.
T_o = 0 # En x=0.
T_l = 0 # En x=L.

x = linspace(0, L, N) # Se discretiza el espacio.
tau = linspace(0, tf, int(tf/dt)) # Se discretiza el tiempo.

def f(x,t):
    c = 0
    for n in range(1,300):
        a = 2*Tin*(1+(-1)**(n+1))/(n*pi)
        s = sin(n*pi*x/L)
        e = exp(-((n*pi/L)**2)*k*t)
        c = c + a*s*e
    return c

ax = plt.axes(projection="3d")

X, Y = meshgrid(x,tau)
Z = f(X,Y)

ax.plot_surface(X, Y, Z, cmap="coolwarm")
ax.set_zlim(0, 110)
ax.set_xlim(0, L)
ax.set_ylim(0, tf)
ax.set_title("Solución analítica.")
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x$')
ax.set_zlabel(r'$T(x,t)$')
ax.view_init(15, 30)
plt.show()
