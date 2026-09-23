dato = input("Ingresa un dato: ")

try:
    dato = int(dato)
    print("Es entero")
    linea = f"{dato}\t\t\n"  

except ValueError:
    try:
        dato = float(dato)
        print("Es un decimal")
        linea = f"\t{dato}\t\n"  
    except ValueError:
        print("Es un texto")
        linea = f"\t\t{dato}\n"  

with open("datos3.txt", "a") as archivo:
   
    if archivo.tell() == 0:
        archivo.write("Enteros\tDecimales\tTextos\n")
        archivo.write("-" * 30 + "\n")
    archivo.write(linea)


with open("datos3.txt", "r") as archivo:
    print("\n" + archivo.read())


    