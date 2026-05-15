import numpy as np

def tabla_diferencias(x, y):
    """Calcula la tabla de coeficientes para la interpolación de Newton."""
    n = len(y)
    coef = np.zeros([n, n])
    # La primera columna es y
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef

def evaluar_newton(coef, x_data, x_interp):
    """Evalúa el polinomio de Newton en x_interp."""
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x_interp - x_data[n - k]) * p
    return p

# --- Ejemplo de uso ---
# Puntos conocidos (x, y)
x = np.array([0.0, 1.0, 2.0])
y = np.array([1.0, 3.0, 6.0])

# Punto a interpolar
x_eval = 1.5

# 1. Obtener coeficientes
coeficientes = tabla_diferencias(x, y)
# Los coeficientes de interés son la primera fila de la matriz diagonal
a = coeficientes[0, :]

# 2. Evaluar el polinomio
y_interp = evaluar_newton(a, x, x_eval)

print(f"Coeficientes: {a}")
print(f"Interpolación en {x_eval}: {y_interp}") # Resultado esperado: 4.25
