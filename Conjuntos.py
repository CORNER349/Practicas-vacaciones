A = set()
B = set()

print("=== CONJUNTO A ===")

cantidad_A = int(input("¿Cuantos elementos tendra A?: "))

for i in range(cantidad_A):
    elemento = input(f"Elemento {i + 1}: ")
    A.add(elemento)

print("\n=== CONJUNTO B ===")

cantidad_B = int(input("¿Cuantos elementos tendra B?: "))

for i in range(cantidad_B):
    elemento = input(f"Elemento {i + 1}: ")
    B.add(elemento)

U = A | B

def caracteristica(x, conjunto):
    if x in conjunto:
        return 1
    else:
        return 0

print("\nConjunto A:", A)
print("Conjunto B:", B)
print("Universo U:", U)

print("\nTABLA DE FUNCIONES CARACTERISTICAS\n")

print(
    f"{'x':<15}"
    f"{'χA(x)':<10}"
    f"{'χB(x)':<10}"
    f"{'A ∩ B':<10}"
    f"{'A ∪ B':<10}"
    f"{'Ac':<10}"
    f"{'Bc':<10}"
)

print("-" * 75)

for x in U:

    chi_A = caracteristica(x, A)
    chi_B = caracteristica(x, B)

    interseccion = chi_A * chi_B

    union = max(chi_A, chi_B)

    complemento_A = 1 - chi_A

    complemento_B = 1 - chi_B

    print(
        f"{x:<15}"
        f"{chi_A:<10}"
        f"{chi_B:<10}"
        f"{interseccion:<10}"
        f"{union:<10}"
        f"{complemento_A:<10}"
        f"{complemento_B:<10}"
    )