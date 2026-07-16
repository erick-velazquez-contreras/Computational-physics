#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:29:48 2024

@author: erickvelazquez
"""
# Estimando la masa de distintas partículas.
from numpy import*
from pylab import*
import pandas as pd
import matplotlib.pyplot as plt


# Primero se lee la información del archivo de texto.
data = pd.read_csv('Jpsimumu_Run2011A.csv')
# Datos de la partícula 1 (energía y momento).
E1 = data.iloc[:,3].values
p1x = data.iloc[:,4].values
p1y = data.iloc[:,5].values
p1z = data.iloc[:,6].values
# Datos de la partícula 2 (energía y momento).
E2 = data.iloc[:,12].values
p2x = data.iloc[:,13].values
p2y = data.iloc[:,14].values
p2z = data.iloc[:,15].values

# Tomamos c = 1.
# Se calculan E_total y p_total.

E = E1 + E2
px = p1x + p2x
py = p1y + p2y
pz = p1z + p2z
p = px**2 + py**2 + pz**2

M = sqrt(E**2 - p)

"""
M = zeros(len(E))
for i in range(len(M)):
    M[i] = sqrt(E[i]**2 - p[i]**2)
"""
# Número de clases.
n_bins = 110
# Histograma.
plt.figure(figsize=(10,6))
hist(M, bins=n_bins, color='skyblue', rwidth=0.5)
plt.xlabel('Masa')
plt.ylabel('Frecuencia')

plt.show()


# Primera resonancia.

start_value = 3
end_value = 3.2

# Se filtran los datos
interval_mask = (M >= start_value) & (M <= end_value)
data_within_interval = M[interval_mask]

#Histograma de datos filtrados
hist, bins = np.histogram(data_within_interval, bins=n_bins)

# Se encuentra el "bin" con frecuencia más alta
max_bin_index = np.argmax(hist)

# Se obtienen los valores que corresponden a la frecuencia más alta
peak_values = (bins[max_bin_index])

print('Primera resonancia.')
print("Valor para el pico más alto en el intervalo [", start_value," , ", end_value," ].")
print("Masa: " , round(peak_values,4))
print(' ')

# Segunda resonancia.

start_value = 3.6
end_value = 3.7


interval_mask = (M >= start_value) & (M <= end_value)
data_within_interval = M[interval_mask]


hist, bins = np.histogram(data_within_interval, bins=n_bins)


max_bin_index = np.argmax(hist)


peak_values = (bins[max_bin_index])
print('Segunda resonancia.')
print("Valor para el pico más alto en el intervalo [", start_value," , ", end_value," ].")
print("Masa: " , round(peak_values,4))