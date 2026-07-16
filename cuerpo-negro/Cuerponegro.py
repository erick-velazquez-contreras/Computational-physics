#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:22:21 2026

@author: erickvelazquez
"""


from numpy import*
from pylab import*

# Datos del COBE: número de onda (1/cm), intensidad (MJy/sr), error (kJy/sr).
nu = array([2.27,2.72,3.18,3.63,4.08,4.54,4.99,5.45,5.90,6.35,6.81,7.26,
            7.71,8.17,8.62,9.08,9.53,9.98,10.44,10.89,11.34,11.80,12.25,
            12.71,13.16,13.61,14.07,14.52,14.97,15.43,15.88,16.34,16.79,
            17.24,17.70,18.15,18.61,19.06,19.51,19.97,20.42,20.87,21.33])

I = array([200.723,249.508,293.024,327.770,354.081,372.079,381.493,383.478,
           378.901,368.833,354.063,336.278,316.076,293.924,271.432,248.239,
           225.940,204.327,183.262,163.830,145.750,128.835,113.568,99.451,
           87.036,75.876,65.766,57.008,49.223,42.267,36.352,31.062,26.580,
           22.644,19.255,16.391,13.811,11.716,9.921,8.364,7.087,5.801,4.523])

errI_kJy = array([14,19,25,23,22,21,18,18,16,14,13,12,11,10,11,12,14,16,18,
                   22,22,23,23,23,22,21,20,19,19,19,21,23,26,28,30,32,33,35,
                   41,55,88,155,282])

sigmaI = errI_kJy/1000   # kJy/sr -> MJy/sr, mismas unidades que I.

# Constantes físicas en CGS.
h = 6.62607015e-27   # erg*s
c = 2.99792458e10    # cm/s
k = 1.380649e-16      # erg/K

# nu esta dado como número de onda (1/cm); la frecuencia real es c*nu.
def g(nu, T):
    nuHz = c*nu
    Icgs = (2*h*nuHz**3/c**2)/(exp(h*nuHz/(k*T)) - 1)   # erg/s/cm^2/Hz/sr
    return Icgs/1e-23/1e6   # -> Jy/sr -> MJy/sr

# Derivada de chi^2 respecto a T (condiciónn de mínimo: f(T) = 0).
def f(T, nu, I):
    return sum((I - g(nu,T))/sigmaI**2*dgdT(nu,T))

def dgdT(nu, T, h_step=1e-3):
    return (g(nu, T + h_step) - g(nu, T - h_step))/(2*h_step)

# Newton Raphson en una dimension
def NRaphson1D(f, T0, nu, I, tol, item):
    T = T0
    hstep = 1e-3
    for it in range(item):
        F  = f(T, nu, I)
        dF = (f(T+hstep, nu, I) - f(T-hstep, nu, I))/(2*hstep)
        Tnuevo = T - F/dF
        if abs(Tnuevo - T) < tol:
            T = Tnuevo
            break
        T = Tnuevo
    return T

T0   = 3.0     # semilla inicial (K), cerca del valor esperado ~2.7 K.
tole = 1e-8
item = 100

Tsol = NRaphson1D(f, T0, nu, I, tole, item)

# chi^2 del ajuste y su incertidumbre (a partir de la curvatura de chi^2).
Imod = g(nu, Tsol)
chi2 = sum(((I - Imod)/sigmaI)**2)
dof  = len(nu) - 1 # número de datos - número de grados de libertad (parámetros ajustados)
chi2_red = chi2/dof #chi^2 reducida

hstep = 1e-2
d2chi2 = (f(Tsol+hstep, nu, I) - f(Tsol-hstep, nu, I))/hstep
sigma_T = sqrt(2/abs(d2chi2))

print('Ajuste espectro de cuerpo negro (Planck) a datos del COBE')
print('T = ', round(Tsol,4), '+/-', round(sigma_T,6), 'K')
print('chi^2 = ', round(chi2,3), '  chi^2_red = ', round(chi2_red,3))
print('\n')

# Grafica de los datos y el ajuste.
nufino = linspace(min(nu), max(nu), 300)

figure(figsize=(8,6))
errorbar(nu, I, yerr=sigmaI, fmt='o', color='k', label='Datos COBE', capsize=3)
plot(nufino, g(nufino, Tsol), color='r', label=f'Ajuste T = {Tsol:.3f} K')
xlabel('Numero de onda (1/cm)')
ylabel('Intensidad (MJy/sr)')
legend()
show()