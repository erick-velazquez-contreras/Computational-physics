#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:33:30 2024

@author: erickvelazquez
"""

from numpy import*
import random as random
import matplotlib.pyplot as plt

Np = 1000 # Número de partículas.
tmax = Np + 100 # Tiempo de simulación.
N_sim = 10 # Número de simulaciones a realizar.

def sim(N, temp):
    
    ni = N # Número inicial de partículas a la izquierda.
    #nd = N - ni # Número inicial de partículas a la derecha.
    ni_res = zeros(temp + 1) # Arreglo para guardar los valores de ni.
    ni_res[0] = ni
    
    for t in range(1, temp+1): # Bucle de tiempo.
        Pr = ni/N # Probabilidad de que una partícula pase de izquierda a derecha.
        x = random.random() # Variable pseudoaleatorio x.
        Prd = (N - ni)/N
        if x <= Pr: # Condición para pasar partículas a la izquierda o derecha.
            ni -= 1
        elif x <= Prd + Pr:
            ni += 1
            
        ni_res[t] = ni
        
    return ni_res

# Para hacer varias simulaciones.
Res = [] # Lista para guardar los resultados.

for i in range(N_sim): # Iteración para varias simulaciones.
    Ni = sim(Np, tmax)
    Res.append(Ni)
    print(Ni)
# Promedio de las simulaciones
prom = mean(Res, axis = 0)

# Solución analítica.
def ani(t, n):
    Sni = (n/2)*(1 + exp(-2*t/n))
    return Sni

tau = arange(tmax+1) # Arreglo de tiempo.
sola = ani(tau, Np) # Evaluación de la sol. analítica.

# Gráfica.

plt.figure(figsize=(10, 6))

for k in range(N_sim):
    plt.plot(tau, Res[k], label = f'Sim. {k+1}')

plt.plot(tau, sola, label='Sol. analítica.', color='r', linestyle='dashed')
plt.plot(tau, prom, label='Promedio.', color='k', linestyle='dashed')

plt.xlabel('Tiempo.')
plt.ylabel('Ni.')
plt.legend()
plt.show()
