#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:42:56 2024

@author: erickvelazquez
"""

# (a) Piones monoenergéticos.

from numpy import *
import random as random

K = 200 # Energía cinética en MeV.
x = 20 # Distancia en metros.
tau = 26 # Tiempo promedio de vida en nanosegundos (en el sistema de referencia del mismo pión).
c = 3e8 # velocidad de la luz.
m = 139.6 # Masa en Mev/c^2.
y = 1/tau # Factor lambda del decaimiento.
np = 1000000 # Número de piones a simular.

gam = K/(m) + 1 # Factor gamma.
# Nótese que por las unidades de m, Eo = mc^2 = m.

v = c*sqrt(1 - 1/(gam**2)) # Velocidad del pión desde el sistema laboratorio.

tl = (x/v)*1e9 # Tiempo de recorrido en el sistema lab. en nanosegundos.

tp = tl/gam #Tiempo de recorrido para el propio pión (tiempo propio).

#print('Factor gamma: ', gam)
#print('Velocidad de pión (lab):', v)
print('Tiempo de recorrido (lab): ', tl)
print('Tiempo propio de recorrido: ', tp) # En nanosegundos.


# Simulación del decaimiento.
def viv(num, t, lam):
    co = num # Contador de piones.
    for i in range(0, t+1): # Bucle de tiempo.
        for j in range(1, num+1): # Bucle de decaimiento.
            dec = random.random() # Valor "aleatorio" para el pión.
            if dec < lam: # Criterio de tiempo de vida.
                co = co -1
        num = co
    return co

res = viv(np,int(tp),y)

print('Factor Lambda: ', round(1/int(tp), 2))
print('Número inicial de piones: ', np)
print('Número de piones que sobreviven: ', res)

