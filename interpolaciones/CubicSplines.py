#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:11:06 2024

@author: erickvelazquez
"""

#Ahora por splines cúbicos.

from numpy import*
from pylab import*
import pandas as pd
from scipy.interpolate import CubicSpline

# Primero se lee la información del archivo de texto BretWigner.
data = pd.read_csv('BretWigner.txt',header=0,delim_whitespace = True)
# Se recopilan los datos de las tres columnas.
E = data.iloc[:,1]
f = data.iloc[:,2]
sig = data.iloc[:,3]

# Interpolación por cubic splines de python.
f_interpol = CubicSpline(E, f, bc_type='natural')

x_cs = linspace(min(E), max(E), 1000) # Domino para hacer la interpolación.
f_cs = f_interpol(x_cs)

# Gráfica.
plt.errorbar(E, f, yerr= sig, fmt="o", color="b", capsize=5) # Puntos experimentales
plot(x_cs, f_cs,':g') # Ajuste. 
xlabel('E')
ylabel('f(E)')
plt.legend(('Ajuste por cubic splines.', 'Datos experimentales.'), shadow=True)
show()

Er = x_cs[argmax(f_cs)] # Energía de resonancia, siendo la correspondiente al valor más alto de pil.
print('Energía de resonancia: ', round(Er,2))

max_value = max(f_cs) # Valor máximo.
max_index = argmax(f_cs) # Índice de valor máximo.

half_max_value = max_value / 2 # Mital del valor máximo
"""
# Se encuentran los puntos a ambos lados del valor máximo a la mitad.
left_index = where(f_cs[:max_index] < half_max_value)[0][-1]
right_index = where(f_cs[max_index:] < half_max_value)[0][0] + max_index

FWHM = x_cs[right_index] - x_cs[left_index]
"""
ind_abhm = where(f_cs > half_max_value)
x_eva= x_cs[ind_abhm]
x_cond = extract(x_eva>40, x_eva)

FWHM = x_cond[-1] - x_cond[0]

print('Full Width at Half Maximum (FWHM):', round(FWHM,2))
