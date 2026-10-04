from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import numpy as np


def regresion_lineal_mnist():

    # ==================================================
    # 1. CARGAR LA BASE DE DATOS MNIST
    # ==================================================

    print("Cargando MNIST...")

    mnist = fetch_openml(
        "mnist_784",
        version=1,
        as_frame=False
    )

    X = mnist.data
    y = mnist.target.astype(int)

    print("\nBase de datos cargada correctamente.")
    print("Cantidad de imágenes:", len(X))
    print("Cantidad de características:", X.shape[1])

    # Cada imagen tiene 28 x 28 = 784 píxeles


    # ==================================================
    # 2. MOSTRAR VALORES ANTES DE NORMALIZAR
    # ==================================================

    print("\nValores de algunos píxeles ANTES de normalizar:")
    print(X[0][:20])


    # ==================================================
    # 3. NORMALIZACIÓN DE LOS PÍXELES
    # ==================================================

    # Los píxeles originalmente tienen valores entre
    # 0 y 255.
    #
    # Se dividen entre 255 para obtener valores
    # entre 0 y 1.

    X = X.astype(float) / 255.0

    print("\nValores de los mismos píxeles DESPUÉS de normalizar:")
    print(X[0][:20])

    print("\nValor mínimo:", X.min())
    print("Valor máximo:", X.max())


    # ==================================================
    # 4. DIVIDIR ENTRENAMIENTO Y PRUEBA
    # ==================================================

    # MNIST contiene 70,000 imágenes.
    #
    # 60,000 entrenamiento
    # 10,000 prueba

    X_train = X[:60000]
    y_train = y[:60000]

    X_test = X[60000:]
    y_test = y[60000:]

    print("\nDatos de entrenamiento:", X_train.shape)
    print("Datos de prueba:", X_test.shape)


    # ==================================================
    # 5. CREAR EL MODELO DE REGRESIÓN LINEAL
    # ==================================================

    modelo = LinearRegression()

    print("\nEntrenando modelo...")

    modelo.fit(X_train, y_train)

    print("Entrenamiento terminado.")


    # ==================================================
    # 6. REALIZAR PREDICCIONES
    # ==================================================

    predicciones = modelo.predict(X_test)

    # La regresión lineal puede producir números
    # decimales como:
    #
    # 4.23
    # 7.81
    # 1.45
    #
    # Los redondeamos al entero más cercano.

    predicciones_redondeadas = np.rint(predicciones)

    # Evitamos valores menores que 0 o mayores que 9

    predicciones_redondeadas = np.clip(
        predicciones_redondeadas,
        0,
        9
    )

    predicciones_redondeadas = predicciones_redondeadas.astype(int)


    # ==================================================
    # 7. CALCULAR MÉTRICAS DE REGRESIÓN
    # ==================================================

    mse = mean_squared_error(
        y_test,
        predicciones
    )

    mae = mean_absolute_error(
        y_test,
        predicciones
    )

    r2 = r2_score(
        y_test,
        predicciones
    )


    # ==================================================
    # 8. CALCULAR ACIERTOS
    # ==================================================

    aciertos = np.sum(
        predicciones_redondeadas == y_test
    )

    total = len(y_test)

    exactitud = aciertos / total * 100


    # ==================================================
    # 9. MOSTRAR RESULTADOS
    # ==================================================

    print("\n==============================")
    print("RESULTADOS DEL MODELO")
    print("==============================")

    print("MSE:", round(mse, 4))
    print("MAE:", round(mae, 4))
    print("R²:", round(r2, 4))

    print("\nAciertos:", aciertos)
    print("Total de pruebas:", total)
    print("Exactitud:", round(exactitud, 2), "%")


    # ==================================================
    # 10. MOSTRAR PREDICCIONES
    # ==================================================

    print("\nPRIMERAS 20 PREDICCIONES\n")

    for i in range(20):

        print(
            "Real:",
            y_test[i],
            "| Predicción:",
            round(predicciones[i], 2),
            "| Redondeado:",
            predicciones_redondeadas[i]
        )


    # ==================================================
    # 11. MOSTRAR ALGUNAS IMÁGENES
    # ==================================================

    for i in range(10):

        imagen = X_test[i].reshape(28, 28)

        plt.figure()

        plt.imshow(
            imagen,
            cmap="gray"
        )

        plt.title(
            "Real: "
            + str(y_test[i])
            + " | Predicción: "
            + str(predicciones_redondeadas[i])
            + " | Valor regresión: "
            + str(round(predicciones[i], 2))
        )

        plt.axis("off")

        plt.show()


# ==================================================
# LLAMAR A LA FUNCIÓN
# ==================================================

regresion_lineal_mnist()