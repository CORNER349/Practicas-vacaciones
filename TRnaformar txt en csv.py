import csv

archivo_txt = "datos3.txt"
archivo_csv = "datos333.csv"

with open(archivo_txt, "r", encoding="utf-8") as txt:
    with open(archivo_csv, "w", newline="", encoding="utf-8") as csvfile:

        lector = csv.reader(txt, delimiter="\t")
        escritor = csv.writer(csvfile)

        for numero_fila, fila in enumerate(lector):

            # Saltar solamente la línea de guiones
            if numero_fila == 1:
                continue

            escritor.writerow(fila)

print("Archivo convertido correctamente.")