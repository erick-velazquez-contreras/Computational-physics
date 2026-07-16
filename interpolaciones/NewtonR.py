#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:25:37 2024

@author: erickvelazquez
"""

from numpy import*
from pylab import*
import pandas as pd


# Primero se lee la información del archivo de texto BretWigner.
data = pd.read_csv('BretWigner.txt',header=0,delim_whitespace = True)
# Se recopilan los datos de las tres columnas.
E = data.iloc[:,1]
efe = data.iloc[:,2]
sigma = data.iloc[:,3]
# Se define la función fundamental.
def g(x, a):
    a1, a2, a3 = a
    return (a1 / ((x - a2)**2 + a3))

# Se definen las funciones que minimizan X^2.
def f1(a, x, y):
    return sum((y[i] - g(x[i], a))/(((x[i] - a[1])**2 + a[2])*sigma[i]**2) for i in range(len(x)))

def f2(a, x, y):
    return sum((y[i] - g(x[i], a))*(x[i] - a[1])/((((x[i] - a[1])*2 + a[2])*2)*sigma[i]**2) for i in range(len(x)))

def f3(a, x, y):
    return sum((y[i] - g(x[i], a))/((((x[i] - a[1])*2 + a[2])*2)*sigma[i]**2) for i in range(len(x)))

# Forward difference.
def fordif(f, a, x, y, h=1e-5):
    n = len(a)
    df = zeros(n)
    for i in range(n):
        aplus = copy(a)
        aplus[i] = aplus[i] + h
        df[i] = (f(aplus, x, y) - f(a, x, y))/h
    return df

# Matriz jacobiana.
def jaco(fl, a, x, y, h=1e-5):
    col = len(a)
    fil = len(fl)
    J = zeros((fil, col))
    for i in range(fil):
        for j in range(col):
            ap = copy(a)
            ap[j] = ap[j] + h
            J[i, j] = (fl[i](ap, x, y) - fl[i](a, x, y))/h
            #J[i][j] = fordif(fl[i](a,x,y), a, x, y) 
    return J

# Algoritmo de Newton Raphson para el caso multidimensional.
def Nera(f_lista, atz, x, y, tol, item):
    a = copy(atz)
    aol = a.astype(float) 
    for k in range(item):
        F = array([f(a, x, y) for f in f_lista])
        J = jaco(f_lista, a, x, y)
        a = linalg.solve(J, -F)
        if linalg.norm(a - aol) < tol:
            break
    return a


a_seed = np.array([7600, 70.0, 600.0]) # Semilla inicial.
# Ésta es bien específica. Es muy fácil dar semillas que lleven a indeterminaciones.

f_lista = [f1, f2, f3]# Lista de funciones

tole = 0.001 # Tolerancia.

item = 100 # Número máximo de iteraciones.

sol = Nera(f_lista, a_seed, E, efe, tole, item)

print("Solución (a1, a2, a3):", sol)
print('fr = ', round(sol[0],3), '\nEr = ', round(sol[1],3), '\nGamma = ', round(sqrt(4*sol[2]),3))
print('\n \n')
