dato = input("Ingresa el primer dato: ")
print(dato)

try:
    dato = int(dato)
    print("Es entero")
    tipo = "Entero"

except ValueError:
    try:
        dato = float(dato)
        print("Es un decimal")
        tipo = "Decimal"

    except ValueError:
        print("Es un texto")
        tipo = "Texto"


with open("datos2.txt", "a") as archivo:
    archivo.write(f"{tipo}: {dato}\n")


with open("datos.txt", "r") as archivo:
    contenido = archivo.read()

print("\n--- Contenido actual de datos.txt ---")
print(contenido)