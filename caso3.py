import numpy as np

# Creamos una matriz 6x6 triangular inferior con unos
def matriz_triangular_inferior():
    matriz = np.tril(np.ones((6, 6)))  # tril genera la matriz triangular inferior
    return matriz

# Mostramos la matriz
matriz = matriz_triangular_inferior()
print(matriz)
