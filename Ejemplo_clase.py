import numpy as np

entradas = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])  # Matriz de entradas, incluyendo el sesgo
salidas_deseadas = np.array([0.0, 1.0, 1.0, 0.0])  # Vector de salidas deseadas
pesos = np.array([0.005, 0.003, -0.001])  # Vector de pesos incluyendo el sesgo
tasa_aprendizaje = 0.01  # Tasa de aprendizaje

# Función propagar
def propagar_ejemplos():
    y_lista = []
    e_lista = []
    e2_lista = []
    
    print(f"{'x0':<4} {'x1':<4} {'x2':<4} {'d':<6} {'y':<10} {'e':<10} {'e^2':<10}")
    print("-" * 52)
    
    for indice_ejemplo in range(4):
        x = entradas[indice_ejemplo]
        d = salidas_deseadas[indice_ejemplo]
        y = np.dot(x, pesos)
        e = d - y
        e2 = e ** 2
        y_lista.append(y)
        e_lista.append(e)
        e2_lista.append(e2)
        print(f"{x[0]:<4} {x[1]:<4} {x[2]:<4} {d:<6.1f} {y:<10.4f} {e:<10.4f} {e2:<10.4f}")
    error_medio = (1 / len(entradas)) * np.sum(e2_lista)
    print("-" * 52)
    print(f"Error Medio Cuadrático <e>: {error_medio:.6f}")

propagar_ejemplos()