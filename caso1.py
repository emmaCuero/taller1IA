#caso 1
def impares_inverso(inicio, fin):
    # Generamos los números impares dentro del rango, recorriendo el rango inversamente
    for numero in range(fin, inicio - 1, -1):
        if numero % 2 != 0:  # Condición para verificar si es impar
            print(numero)

# Ejemplo: imprimir los números impares entre 1 y 20 de manera inversa
impares_inverso(1, 20)

#caso 2

def impares_inverso(inicio, fin):
    impares = [str(numero) for numero in range(fin, inicio - 1, -1) if numero % 2 != 0]
    print(", ".join(impares))

# Ejemplo: imprimir los números impares entre 1 y 20 de manera inversa, separados por comas
impares_inverso(1, 20)
