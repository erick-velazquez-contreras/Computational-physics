#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:58:17 2024

@author: erickvelazquez
"""

# Vibración de una cuerda.

from numpy import*
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Datos iniciales.

L = 10 # Longitud de la cuerda.
N = 100 # Número de puntos en los que dividimos la cuerda.
tf = 30 # Tiempo de simulación.
c = 1 # velocidad de la onda viajera.
dx = L/(N-1) # Paso espacial.
dt = 0.01 # Paso temporal.
cp = dx/dt


# Recuerda la condición de Courant: c/cp <= 1, i.e. dx/dt >= c.

# Condiciones de frontera.
y_o = 0
y_l = 0

# Discretización de espacio y tiempo.
x = linspace(0, L, N)
t = linspace(0, tf, int(tf/dt))

# Matriz de desplazamientos transversales en la cuerda.
y = zeros((size(x), size(t)))

# Condiciones iniciales.

def inic(x,L):
    if x <= 0.5*L:
        r = (2/L)*x
    else:
        r = -(2/L)*x + 2
    return r

# Se llenan las condiciones iniciales con la función definida por inic.
for i in range(1, size(x)):
    y[i,0] = inic(x[i], L)


# Condiciones de frontera.
y[0,:] = y_o
y[-1,:] = y_l

#Como el método es de tres pasos, para t=2, se necesita información en t=0 y t=1.
#Así que calculamos y[i,1] de forma independiente, tomando en cuenta que
# y[i, 1] = y[i, -1] por la condición inicial y_t(x,t=o) = 0 = (y[i, 1] - y[i, -1])/2dt (central difference)

velo = (c/cp)**2
for i in range(1, size(x)-1):
    y[i, 1] = y[i, 0] + 0.5*velo*(y[i+1, 0] + y[i-1, 0] - 2*y[i, 0])


# Para ver la forma inicial de la cuerda.
plt.plot(x, y[:, 0])
plt.xlabel('Position (m)')
plt.ylabel('Displacement')
plt.title('Initial Shape of the String')
plt.show()

# Se aplica el método numérico.
for j in range(1, size(t)-1):
    for i in range(1, size(x)-1):
        y[i, j+1] = 2*y[i, j] - y[i, j-1] + ((c*dt/dx)**2) * (y[i+1, j] + y[i-1, j] - 2*y[i, j])

# Función para ir actualizando la gráfica.
def update_plot(frame):
    plt.clf()  # Clear the current figure
    plt.plot(x, y[:, frame])  # Plot the string displacement at the current frame
    plt.xlabel('Position (m)')
    plt.ylabel('Displacement')
    plt.title(f'Time = {frame * dt:.2f} s')  # Update the title with the current time
    plt.ylim(-3, 3)  # Adjust the y-axis limits if needed

# Se hace la animación.
animation = anim.FuncAnimation(plt.figure(), update_plot, frames=len(t), interval=50)

plt.show()

print(c/cp)