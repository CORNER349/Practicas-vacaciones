import math
import random

cantidad=100
for i in range(cantidad):
    tipo = random.choice(["entero", "decimal", "texto", "imc"])
    if tipo == "entero":
        dato = random.randint(1, 100)
        linea = f"{dato}\t\t\t\t\t\t\t\t\t\t\n"
    elif tipo == "decimal":
        dato = round(random.uniform(1, 100), 2)
        linea = f"\t{dato}\t\t\t\t\t\t\t\t\t\n"
    elif tipo == "texto":
        palabras = [
            "hola",
            "python",
            "IA",
            "datos",
            "programacion",
            "computadora",
            "universidad",
            "algoritmo"
        ]
        dato = random.choice(palabras)
        linea = f"\t\t{dato}\t\t\t\t\t\t\t\t\n"

    elif tipo == "imc":
        peso = round(random.uniform(50, 100), 2)
        altura = round(random.uniform(1.50, 2.00), 2)
        imc = round(peso / (altura ** 2), 2)
        linea = f"\t\t\t\t\t\t\t\t{peso}\t{altura}\t{imc}\n"


    with open("datos3.txt", "a") as archivo:
        archivo.write(linea)


try:
    with open("datos3.txt", "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    lineas = []
resultado = []

resultado.append(
    "Entero\tDecimal\tTexto\tSuma\tResta\tMult\tDiv\tRaiz\tPeso\tAltura\tIMC\n"
)
resultado.append("-" * 90 + "\n")

for linea in lineas:
    linea = linea.strip("\n")
    if linea.startswith("Entero") or linea.startswith("-") or not linea.strip():
        continue
    partes = linea.split("\t")
    entero_txt = partes[0].strip() if len(partes) > 0 else ""
    decimal_txt = partes[1].strip() if len(partes) > 1 else ""
    texto_txt = partes[2].strip() if len(partes) > 2 else ""
    peso_txt = partes[8].strip() if len(partes) > 8 else ""
    altura_txt = partes[9].strip() if len(partes) > 9 else ""
    imc_txt = partes[10].strip() if len(partes) > 10 else ""
    val_entero = int(entero_txt) if entero_txt else 0
    val_decimal = float(decimal_txt) if decimal_txt else 0
    suma = "-"
    resta = "-"
    mult = "-"
    div = "-"
    raiz = "-"

    if entero_txt or decimal_txt:
        suma = str(val_entero + val_decimal)
        resta = str(val_entero - val_decimal)
        mult = str(val_entero * val_decimal)
        if val_decimal != 0:
            div = str(round(val_entero / val_decimal, 2))
        else:
            div = "Err"

        if entero_txt:
            val_raiz = val_entero
        else:
            val_raiz = val_decimal
        if val_raiz >= 0:
            raiz = str(round(math.sqrt(val_raiz), 2))
        else:
            raiz = "Err"
    nueva_fila = (
        f"{entero_txt}\t"
        f"{decimal_txt}\t"
        f"{texto_txt}\t"
        f"{suma}\t"
        f"{resta}\t"
        f"{mult}\t"
        f"{div}\t"
        f"{raiz}\t"
        f"{peso_txt}\t"
        f"{altura_txt}\t"
        f"{imc_txt}\n"
    )

    resultado.append(nueva_fila)

with open("datos3.txt", "w") as archivo:
    archivo.writelines(resultado)



with open("datos3.txt", "r") as archivo:
    print(archivo.read())