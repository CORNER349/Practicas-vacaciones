dato=input("Ingresa el primer dato")
print(dato)
x=[]
y=[]
z=[]
try:
    dato=int(dato)
    print("Es entero")
    x=dato
except ValueError:
    try:
        dato=float(dato)
        print("Es un decimal")
        y=dato
    except ValueError:
        print("Es un texto")
        z=dato