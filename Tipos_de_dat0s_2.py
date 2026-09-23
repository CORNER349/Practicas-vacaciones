import math
dato = input("Ingresa un dato: ")

try:
    dato = int(dato)
    print("Es entero")
    linea = f"{dato}\t\t\n"

except ValueError:
    try:
        dato = float(dato)
        print("Es decimal")
        linea = f"\t{dato}\t\n"

    except ValueError:
        print("Es texto")
        linea = f"\t\t{dato}\n"

with open("datos3.txt", "a") as archivo:
    archivo.write(linea)

with open("datos3.txt", "r") as archivo:
    lineas = archivo.readlines()

resultado = []
resultado.append(
    "Entero\tDecimal\tTexto\tSuma\tResta\tMult\tDiv\tRaiz\n"
)
resultado.append("-" * 65 + "\n")

for linea in lineas:
    linea = linea.strip("\n")
    if linea.startswith("Entero") or linea.startswith("-") or not linea.strip():
        continue

    partes = linea.split("\t")

    entero_txt = partes[0].strip() if len(partes) > 0 else ""
    decimal_txt = partes[1].strip() if len(partes) > 1 else ""
    texto_txt = partes[2].strip() if len(partes) > 2 else ""

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
            raiz = str(round(math.sqrt(val_entero), 2))

        elif decimal_txt:
            raiz = str(round(math.sqrt(val_decimal), 2))

    nueva_fila = (
        f"{entero_txt}\t"
        f"{decimal_txt}\t"
        f"{texto_txt}\t"
        f"{suma}\t"
        f"{resta}\t"
        f"{mult}\t"
        f"{div}\t"
        f"{raiz}\n"
    )

    resultado.append(nueva_fila)

with open("datos3.txt", "w") as archivo:
    archivo.writelines(resultado)

with open("datos3.txt", "r") as archivo:
    print("\n" + archivo.read())