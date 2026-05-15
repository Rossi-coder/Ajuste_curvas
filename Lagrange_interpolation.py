import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x_val):
    """Calcula el valor interpolado en x_val usando puntos (x_points, y_points)"""
    n = len(x_points)
    result = 0
    
    for i in range(n):
        # Calcular los polinomios fundamentales de Lagrange L_i(x)
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x_points[j]) / (x_points[i] - x_points[j])
        result += term
        
    return result

# 1. Puntos de datos conocidos (Nodos)
x_nodos = np.array([0, 1, 2, 4])
y_nodos = np.array([1, 3, 2, 5])

# 2. Generar puntos para graficar la curva
x_graf = np.linspace(min(x_nodos), max(x_nodos), 100)
y_graf = [lagrange_interpolation(x_nodos, y_nodos, x) for x in x_graf]

# 3. Visualización
plt.figure(figsize=(8, 5))
plt.plot(x_graf, y_graf, label='Polinomio de Lagrange', color='blue')
plt.scatter(x_nodos, y_nodos, label='Nodos', color='red')
plt.title('Interpolación de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
