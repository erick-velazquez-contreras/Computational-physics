#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: erickvelazquez
"""


from numpy import*
from pylab import*

# Datos del experimento (tiempo en ns, voltaje en volts, incertidumbre en volts).
t = array([0.0, 32.8, 65.6, 98.4, 131.2, 164.0, 196.8, 229.6, 262.4,
           295.2, 328.0, 360.8, 393.6, 426.4, 459.2, 492.0])

V = array([5.08e+00, 3.29e+00, 2.23e+00, 1.48e+00, 1.11e+00, 6.44e-01,
           4.76e-01, 2.73e-01, 1.88e-01, 1.41e-01, 9.42e-02, 7.68e-02,
           3.22e-02, 3.22e-02, 1.98e-02, 1.98e-02])

sigmaV = array([1.12e-01, 9.04e-02, 7.43e-02, 6.05e-02, 5.25e-02, 4.00e-02,
                3.43e-02, 2.60e-02, 2.16e-02, 1.87e-02, 1.53e-02, 1.38e-02,
                8.94e-03, 8.94e-03, 7.01e-03, 7.01e-03])

# El modelo V(t) = V0*exp(-Gamma*t) es no lineal, pero al tomar ln:
# ln(V) = ln(V0) - Gamma*t
# se vuelve lineal en los parametros (a = ln(V0), b = -Gamma).
# Propagamos la incertidumbre: sigma_lnV = sigmaV/V.

y = log(V)
sigmaY = sigmaV/V

# Ajuste lineal ponderado y = a + b*t, minimizando chi^2
w = 1/sigmaY**2

S   = sum(w)
Sx  = sum(w*t)
Sy  = sum(w*y)
Sxx = sum(w*t**2)
Sxy = sum(w*t*y)

Delta = S*Sxx - Sx**2

b = (S*Sxy - Sx*Sy)/Delta       # b = -Gamma
a = (Sxx*Sy - Sx*Sxy)/Delta     # a = ln(V0)

sigma_b = sqrt(S/Delta)
sigma_a = sqrt(Sxx/Delta)

Gamma  = -b
V0     = exp(a)

sigma_Gamma = sigma_b
sigma_V0    = V0*sigma_a        # propagacion: V0 = exp(a) -> sigma_V0 = V0*sigma_a

# chi^2 del ajuste (evaluado sobre los datos originales, no en el espacio log).
Vmod = V0*exp(-Gamma*t)
chi2 = sum(((V - Vmod)/sigmaV)**2)
dof  = len(t) - 2   # dos parametros ajustados (V0, Gamma)
chi2_red = chi2/dof

print('Ajuste V(t) = V0*exp(-Gamma*t)')
print('V0    = ', round(V0,4), '+/-', round(sigma_V0,4), 'V')
print('Gamma = ', round(Gamma,6), '+/-', round(sigma_Gamma,6), '1/ns')
print('chi^2 = ', round(chi2,3), '  chi^2_red = ', round(chi2_red,3))
print('\n')

# Grafica semi-log con barras de error y el ajuste sobreimpuesto.
tfino = linspace(0, max(t), 300)

figure(figsize=(8,6))
errorbar(t, V, yerr=sigmaV, fmt='o', color='k', label='Datos', capsize=3)
plot(tfino, V0*exp(-Gamma*tfino), color='r', label='Ajuste')
yscale('log')
xlabel('Tiempo (ns)')
ylabel('Voltaje (V)')
legend()
show()