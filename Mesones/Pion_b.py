#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:10:58 2024

@author: erickvelazquez
"""

# (b) Piones con distribución gaussiana de energías.

from numpy import *
import random as random

Em = 200 # Valor medio de energía en MeV.
sig = 50
x = 20 # Distancia en metros.
tau = 26 # Tiempo promedio de vida en nanosegundos (en el sistema de referencia del mismo pión).
c = 3e8 # velocidad de la luz.
m = 139.6 # Masa en Mev/c^2.
y = 1/tau # Factor lambda del decaimiento.
np = 1000000 # Número de piones a simular.

# Función para calcular el tiempo propio de recorrido.
def tpr(k, er, d):
    gam = k/er + 1
    v = c*sqrt(1 - 1/(gam**2))
    tl = (x/v)*1e9
    tp = tl/gam
    return(int(tp))

# Simulación del decaimiento.
# Como el tiempo depende del pión, se intercambia el orden de los bucles.

def viv(num, lam, er, d):
    co = num # Contador de piones.
    for i in range( num): # Ahora se hace el barrido por partícula, y luego el de tiempo.
        E = random.gauss(Em, sig)
        #print(E)
        if E < 0: # Resulta que salen energías negativas.
            E = -E 
        for j in range(tpr(E, er, d)+1): 
            dec = random.random() # Valor "aleatorio" para el pión.
            if dec < lam: # Criterio de tiempo de vida.
                co = co -1
                break # Si este pión no sobrevive, termina con el bucle y se pasa al siguiente.
        num = co
    return co

res = viv(np, y, m, x)

print('Número de sobrevivientes: ', res)