import numpy as np
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)
y = np.array([0, 0, 0, 1], dtype=float)
w1 = 0.0
w2 = 0.0
b = 0.0
alpha = 0.5
epocas = 1000
def sigmoide(z):
    return 1 / (1 + np.exp(-z))
print("TABLA DE MODIFICACIÓN DE PESOS - AND")
print("Epoca\tw1\t\tw2\t\tBias\t\tError")
for epoca in range(epocas):
    z = w1 * X[:, 0] + w2 * X[:, 1] + b
    prediccion = sigmoide(z)
    error = prediccion - y
    dw1 = np.mean(error * X[:, 0])
    dw2 = np.mean(error * X[:, 1])
    db = np.mean(error)
    w1 = w1 - alpha * dw1
    w2 = w2 - alpha * dw2
    b = b - alpha * db
    perdida = -np.mean(
        y * np.log(prediccion + 1e-8) +
        (1 - y) * np.log(1 - prediccion + 1e-8)
    )
    if epoca < 10:
        print(
            f"{epoca + 1}\t"
            f"{w1:.4f}\t\t"
            f"{w2:.4f}\t\t"
            f"{b:.4f}\t\t"
            f"{perdida:.4f}"
        )
print("\nPesos finales:")
print("w1 =", w1)
print("w2 =", w2)
print("Bias =", b)
print("\nPredicciones:")
for entrada in X:
    z = w1 * entrada[0] + w2 * entrada[1] + b
    salida = sigmoide(z)
    resultado = 1 if salida >= 0.5 else 0
    print(
        entrada,
        "->",
        round(salida, 4),
        "->",
        resultado
    )