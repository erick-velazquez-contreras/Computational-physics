# Decaimiento de voltaje en un circuito RL

Ajuste de mínimos cuadrados al voltaje inducido en un circuito RL en serie que decae exponencialmente en el tiempo según V(t) = V_0*e^(-Gamma*t), donde Gamma = R/L.

El modelo es no lineal en Gamma, pero al tomar logaritmo natural (ln V = ln V_0 - Gamma*t) se convierte en un ajuste lineal ponderado, resuelto directamente con el método de mínimos cuadrados.

## Resultado
V₀ = 5.00 ± 0.08 V
Gamma = 0.01214 ± 0.00016 ns^-1
Chi^2_red ≈ 0.85 

## Archivos
- `Inerpolaciones.pdf` — enunciado del problema (problema 4)
- `volt-ind.py` — implementación numérica
