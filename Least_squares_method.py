
import numpy as np
import matplotlib.pyplot as plt

# 1. Datos de ejemplo
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1, 2.1, 2.9, 4.2, 5.1, 5.8])

# 2. Ajuste por mínimos cuadrados (grado 1 para línea recta)
# m = pendiente, c = intercepto
m, c = np.polyfit(x, y, 1)

print(f"Pendiente (m): {m:.4f}")
print(f"Intercepto (c): {c:.4f}")
print(f"Ecuación: y = {m:.4f}x + {c:.4f}")

# 3. Generar línea de ajuste
y_pred = m * x + c

# 4. Graficar
plt.scatter(x, y, color='red', label='Datos reales')
plt.plot(x, y_pred, color='blue', label=f'Ajuste: y={m:.2f}x+{c:.2f}')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste de Recta por Mínimos Cuadrados')
plt.grid(True)
plt.show()
