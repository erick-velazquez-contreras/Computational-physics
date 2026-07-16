#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:07:32 2026

@author: erickvelazquez
"""

from numpy import*
from pylab import*
from scipy import optimize
from scipy import integrate

# Se define la distribución de Fermi-Dirac.
def FD(E, mu, kT = 0.025):
    fac = exp((E - mu)/kT) + 1
    return 1/fac

# Esta función integra FD en un intervalo definido.
def inte(mu, Emin = 0.0, Emax = 2.0):
    res = integrate.quad(FD, Emin, Emax, args=(mu)) 
    return res[0] - 1 #Es el primer valor de la tupla regresada el que contiene el valor de la integral.
# Aquí se restó 1 porque quereremos ajustar el valor de mu para que se cumpla que
# integral(FD)dE = 1, entonces debe cumplirse que  integral(FD)dE - 1 = 0,
# o sea que estamos buscando una raiz.


m0 = 1.0; dx=3.e-4;err=0.001;Nmax=100;  # Parámetros. m0 es la semilla.
# Función para aplicar el método de Newton -Raphson.
def NewtonR(x,dx,err,Nmax):
    for it in range(0,Nmax+1):
        F = inte(x)
        if (abs(F)<=err):         # ¿Es raíz dentro del error?  
            #print('\n Raíz encontrada, f(raíz)=',F,'Raíz=',x,', error=',err) 
            break
        print('Iteracion=',it,'x=',x,'f(x)=',F)
        df=(inte(x+dx/2)-inte(x-dx/2))/dx  # Central difference
        dx=-F/df 
        x+=dx                         # Nueva propuesta
    if it==Nmax+1: 
        print('\n Newton no encontró raíz para Nmax=',Nmax) 
    return x

m = NewtonR(m0,dx,err,Nmax) # Se guarda el valor de mu encontrado.
print('Valor de mu: ', m)

Er = linspace(0, 2, 100) # Se hace el arreglo de energía para graficar.

y = FD(Er, m) # Se evalúa la función FD en Er con el valor de mu encontrado.

# Se grafica.
plot(Er, y, linestyle='dashed', color='k')
xlabel('E'); ylabel('f(E)')
show()