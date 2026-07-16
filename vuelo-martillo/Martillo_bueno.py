#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:50:48 2026

@author: erickvelazquez
"""

# 1. Lanzamiento de martillo (pulido).
from numpy import *
from pylab import *

# Coeficientes
N = 1000            # Número de pasos.
p = 1.2              # Densidad del medio. 1.2 kg/m^3 para el aire.
R = 0.06             # Radio del martillo. 6 cm = 0.06 m.
phi = 45             # Ángulo de lanzamiento con respecto a la horizontal en grados.
th = phi*pi/180      # Conversión del ángulo a radianes.
m = 7.26             # Masa del martillo en kilogramos.
g = 9.8              # Aceleración por gravedad.
xo = 0               # Posición inicial 'x'.
yo = 2               # Posición inicial 'y'.
tf = 4.3             # tiempo simulación en segundos.
h = tf/(N-1)
v0 = 28.83           # Velocidad inicial en m/s.

def k_de(Cd):
    return 0.5*p*(pi*R**2)*Cd   # Coeficiente de la fuerza de fricción.

# Se definen las ecuaciones diferenciales para las dinámicas en 'x' y 'y'
def edox(est, tau, k):
    fx0 = est[1]
    fx1 = -(k/m)*est[1]*abs(est[1])
    return array([fx0, fx1])

def edoy(est, tau, k):
    fy0 = est[1]
    fy1 = -(k/m)*est[1]*abs(est[1]) - g
    return array([fy0, fy1])

def eux(x, t, h, f, k):
    xp = x + h*f(x, t, k)
    return xp

def simular(Cd, N_max=N):

    k = k_de(Cd)
    y = zeros([N_max, 2])
    x = zeros([N_max, 2])
    t = zeros(N_max)

    x[0, 0] = xo
    y[0, 0] = yo
    x[0, 1] = v0*cos(th)
    y[0, 1] = v0*sin(th)
    
    #Se resuelven las evoluciones en 'x' y 'y'
    #Se detecta cuando 'y' toca el suelo
    n_usados = 0
    for i in range(N_max - 1):
        x[i+1] = eux(x[i], t[i], h, edox, k)
        y[i+1] = eux(y[i], t[i], h, edoy, k)
        t[i+1] = t[i] + h
        if y[i+1, 0] < 0:
            n_usados = i + 1
            break

    # Recortamos los arreglos al número de pasos realmente usados
    t, x, y = t[:n_usados+1], x[:n_usados+1], y[:n_usados+1]

    # Interpolación lineal para obtener posición de aterrizaje
    ypos = y[:, 0]
    if ypos[-1] < 0:
        frac = ypos[-2] / (ypos[-2] - ypos[-1])
        t_ate = t[-2] + frac*(t[-1] - t[-2])
        x_ate = x[-2, 0] + frac*(x[-1, 0] - x[-2, 0])
    else:
        t_ate, x_ate = t[-1], x[-1, 0]  # no llegó a tocar el suelo dentro de N_max pasos

    return t, x, y, n_usados, t_ate, x_ate

regimenes = {'Sin fricción': 0.0, 'Flujo laminar (Cd=0.5)': 0.5, 'Flujo inestable oscilante (Cd=0.75)': 0.75}

resultados = {}
for nombre, Cd in regimenes.items():
    t, x, y, n_usados, t_ate, x_ate = simular(Cd)
    ym = y[:, 0].max()
    resultados[nombre] = (t, x, y, ym, t_ate, x_ate)
    print(f"{nombre}: altura máxima = {ym:.2f} m | aterrizaje: t = {t_ate:.3f} s, x = {x_ate:.2f} m "
          f"| se detuvo en {n_usados} de {N} pasos disponibles")

# Gráficas y-t y trayectoria y=y(x) para los tres regímenes 
fig, ax = subplots(1, 2, figsize=(11, 4.5))
for nombre, (t, x, y, ym, t_ate, x_ate) in resultados.items():
    ax[0].plot(t, y[:, 0], label=nombre)
    ax[1].plot(x[:, 0], y[:, 0], label=nombre)

ax[0].set_xlabel('t (s)'); ax[0].set_ylabel('y (m)'); ax[0].set_title('Altura vs tiempo')
ax[0].axhline(0, color='k', linewidth=0.7)
ax[0].legend()

ax[1].set_xlabel('x (m)'); ax[1].set_ylabel('y (m)'); ax[1].set_title('Trayectoria y = y(x)')
ax[1].axhline(0, color='k', linewidth=0.7)
ax[1].legend()

tight_layout()
show()

# Distancia real de aterrizaje vs Cd (en vez de x(tf) fijo) 
Cds = list(regimenes.values())
xs_aterrizaje = [resultados[n][5] for n in regimenes]
coef = polyfit(Cds, xs_aterrizaje, 1)
print(f"\nAjuste lineal (usando distancia real de aterrizaje): Xmax = {coef[0]:.2f}*Cd + {coef[1]:.2f}")