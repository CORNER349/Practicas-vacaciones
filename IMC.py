import math

while True:
    print("1. Agregar un dato (Entero, Decimal o Texto)")
    print("2. Calcular IMC (Peso, Altura e IMC)")
    print("3. Salir")

    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        dato = input("Ingresa un dato: ")

        try:
            dato = int(dato)
            print("Es entero")
            linea = f"{dato}\t\t\t\t\t\n"

        except ValueError:
            try:
                dato = float(dato)
                print("Es decimal")
                linea = f"\t{dato}\t\t\t\t\n"

            except ValueError:
                print("Es texto")
                linea = f"\t\t{dato}\t\t\t\n"

        with open("datos3.txt", "a") as archivo:
            archivo.write(linea)

    elif opcion == "2":
        try:
            peso = float(input("Ingresa tu peso en kg: "))
            altura = float(input("Ingresa tu altura en metros: "))

            if altura <= 0:
                print("La altura debe ser mayor a cero.")
                continue

            imc = round(peso / (altura ** 2), 2)
            print(f"Tu IMC es: {imc}")

            # Formato: Entero, Decimal, Texto, (Suma/Resta/Mult/Div/Raiz vacíos), Peso, Altura, IMC
            linea = f"\t\t\t\t\t\t\t\t{peso}\t{altura}\t{imc}\n"

            with open("datos3.txt", "a") as archivo:
                archivo.write(linea)

        except ValueError:
            print("Error: Debes ingresar números válidos para peso y altura.")
            continue

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
        continue

    # --- Procesamiento del archivo ---
    try:
        with open("datos3.txt", "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        lineas = []

    resultado = []
    # Encabezados con Peso, Altura e IMC al final
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