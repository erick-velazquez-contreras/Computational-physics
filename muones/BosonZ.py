#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:41:52 2024

@author: erickvelazquez
"""

# Estimando la masa del bosón Z.

from numpy import*
import pandas as pd
from pylab import*
import matplotlib.pyplot as plt

# Primero se lee la información del archivo de texto.
data = pd.read_csv('MuRun2010B.csv')
# Datos del muón 1 (energía y momento).
E1 = data.iloc[:,3].values
p1x = data.iloc[:,4].values
p1y = data.iloc[:,5].values
p1z = data.iloc[:,6].values
# Datos del muón 2 (energía y momento).
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

# Masa estimada de Z.
M = sqrt(E**2 - p)

# Número de clases.
n_bins = 110

"""
# Histograma.
plt.figure(figsize=(10,6))
hist(M, bins=n_bins, color='goldenrod', rwidth=0.5)
plt.xlabel('Masa')
plt.ylabel('Frecuencia')

plt.show()

plt.yscale('log')
"""

# Compute histogram values
hist_values, bin_edges = np.histogram(M, bins=n_bins)

# Transformación logarítmica a las frecuencias
log_hist_values = np.log(hist_values)

# figura del histogrma original
plt.figure(figsize=(14, 6))

# Histograma original.
plt.subplot(1, 2, 1)
plt.hist(M, bins=n_bins, color='goldenrod', rwidth=0.5)
plt.xlabel('Masa')
plt.ylabel('Frecuencia')
plt.title('Histograma Original')

# Histograma logarítmico.
plt.subplot(1, 2, 2)
plt.bar(bin_edges[:-1], log_hist_values, width=(bin_edges[1]-bin_edges[0]), color='skyblue')
plt.xlabel('Masa')
plt.ylabel('Log Frecuencia')
plt.title('Histograma con Frecuencia Logarítmica')

plt.tight_layout()
plt.show()


# Primera resonancia.
start_value = 1.5
end_value = 4

# Filtración de datos
interval_mask = (M >= start_value) & (M <= end_value)
data_within_interval = M[interval_mask]

# Histograma de datos filtrados
hist, bins = np.histogram(data_within_interval, bins=n_bins)

# Encontramos la región con la frecuencia más alta
max_bin_index = np.argmax(hist)

# Valores correspondientes a las frecuencias más altas en el intervalo
peak_values = (bins[max_bin_index])

print('Primera resonancia.')
print("Valor para el pico más alto en el intervalo [", start_value," , ", end_value," ].")
print("Masa: " , round(peak_values,4))
print(' ')

# Segunda resonancia.

start_value = 87
end_value = 95


interval_mask = (M >= start_value) & (M <= end_value)
data_within_interval = M[interval_mask]


hist, bins = np.histogram(data_within_interval, bins=n_bins)


max_bin_index = np.argmax(hist)


peak_values = (bins[max_bin_index])
print('Segunda resonancia.')
print("Valor para el pico más alto en el intervalo [", start_value," , ", end_value," ].")
print("Masa: " , round(peak_values,4))