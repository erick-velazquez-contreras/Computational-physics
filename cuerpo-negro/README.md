# Espectro de cuerpo negro — datos del COBE

Ajuste de la ley de radiación de Planck al espectro de la radiación cósmica de fondo medido por el satélite COBE, para estimar su temperatura.
El modelo de Planck I(nu,T) es no lineal, pero con un único parámetro libre (T), así, se minimizó Chi^2 encontrando la raíz de su derivada respecto a T mediante Newton Raphson en una dimensión — un caso reducido del método multidimensional usado en el ajuste de Breit-Wigner (ver carpeta `interpolaciones/`).

## Resultado
T = 2.725 K — coincide con el valor real medido por el experimento COBE para la temperatura de la radiación cósmica de fondo.
χ²_red ≈ 1.07

## Archivos
- `Inerpolaciones.pdf` — enunciado del problema (problema 5)
- `Cuerponegro.py` — implementación del código
