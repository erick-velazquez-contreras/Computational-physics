#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:46:13 2024

@author: erickvelazquez
"""

from numpy import*
from pylab import*

# Función para hacer interpolación de Lagrange en un punto 'p' a partir de datos 'x' y su respectivo
# contradomino 'f'.
def lagrange(p,x,f):
    s = 0
    n = size(x)
    L = zeros(n) + 1
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                L[i] = L[i]*(p - x[j])/(x[i]-x[j])
        s = s + (f[i]*L[i])
    return s

# Datos experimentales.

E = [0, 25, 50, 75, 100, 125, 150, 175, 200] # Energías.
fe = [10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7] # Sección eficaz.
sig = [9.34, 17.9, 41.5, 85.5, 51.5, 21.5, 10.8, 6.29, 4.14] # Incertidumbre.

xl = arange(0, 205, 5) # Domino para interpolar, de 0 a 200, con paso de 5 MeV.
pil = zeros(size(xl)) # Arreglo vacío de los valores de interpolación.

# Se llenan las entradas de interpolación.
for i in range(size(xl)):
    pil[i] = lagrange(xl[i],E,fe)
    
# Gráfica.
plt.errorbar(E, fe, yerr= sig, fmt="d", color="b", capsize=5) # Puntos experimentales
plot(xl, pil,':r') # Ajuste. 
xlabel('E')
ylabel('f(E)')
plt.legend(('Ajuste por PIL.', 'Datos experimentales.'), shadow=True)
show()


Er = xl[argmax(pil)] # Energía de resonancia, siendo la correspondiente al valor más alto de pil.

half_max = max(pil) / 2

ind_abhm = where(pil > half_max)
x_eva= xl[ind_abhm]
x_cond = extract(x_eva>40, x_eva)

FWHM = x_cond[-1] - x_cond[0]

print('Energía de resonancia:',Er)
print('FWHM: ',round(FWHM,2))

