from itertools import product

def normalizar(expresion):
    """
    Elimina espacios y permite escribir algunos símbolos
    de distintas formas.
    """

    expresion = expresion.upper()
    expresion = expresion.replace(" ", "")

    expresion = expresion.replace("&", "∩")
    expresion = expresion.replace("|", "∪")

    expresion = expresion.replace("^C", "ᶜ")

    expresion = expresion.replace("{}", "∅")

    return expresion

propiedades = {

    "A∩B": {
        "nombre": "Conmutatividad",
        "equivalente": "B∩A",
        "variables": 2,
        "f1": lambda A, B: A and B,
        "f2": lambda A, B: B and A
    },

    "B∩A": {
        "nombre": "Conmutatividad",
        "equivalente": "A∩B",
        "variables": 2,
        "f1": lambda A, B: B and A,
        "f2": lambda A, B: A and B
    },

    "A∪B": {
        "nombre": "Conmutatividad",
        "equivalente": "B∪A",
        "variables": 2,
        "f1": lambda A, B: A or B,
        "f2": lambda A, B: B or A
    },

    "B∪A": {
        "nombre": "Conmutatividad",
        "equivalente": "A∪B",
        "variables": 2,
        "f1": lambda A, B: B or A,
        "f2": lambda A, B: A or B
    },

    "A∩(B∩C)": {
        "nombre": "Asociatividad",
        "equivalente": "(A∩B)∩C",
        "variables": 3,
        "f1": lambda A, B, C: A and (B and C),
        "f2": lambda A, B, C: (A and B) and C
    },

    "(A∩B)∩C": {
        "nombre": "Asociatividad",
        "equivalente": "A∩(B∩C)",
        "variables": 3,
        "f1": lambda A, B, C: (A and B) and C,
        "f2": lambda A, B, C: A and (B and C)
    },

    "A∪(B∪C)": {
        "nombre": "Asociatividad",
        "equivalente": "(A∪B)∪C",
        "variables": 3,
        "f1": lambda A, B, C: A or (B or C),
        "f2": lambda A, B, C: (A or B) or C
    },

    "(A∪B)∪C": {
        "nombre": "Asociatividad",
        "equivalente": "A∪(B∪C)",
        "variables": 3,
        "f1": lambda A, B, C: (A or B) or C,
        "f2": lambda A, B, C: A or (B or C)
    },


    "A∩(B∪C)": {
        "nombre": "Distributividad",
        "equivalente": "(A∩B)∪(A∩C)",
        "variables": 3,
        "f1": lambda A, B, C: A and (B or C),
        "f2": lambda A, B, C: (A and B) or (A and C)
    },

    "(A∩B)∪(A∩C)": {
        "nombre": "Distributividad",
        "equivalente": "A∩(B∪C)",
        "variables": 3,
        "f1": lambda A, B, C: (A and B) or (A and C),
        "f2": lambda A, B, C: A and (B or C)
    },

    "A∪(B∩C)": {
        "nombre": "Distributividad",
        "equivalente": "(A∪B)∩(A∪C)",
        "variables": 3,
        "f1": lambda A, B, C: A or (B and C),
        "f2": lambda A, B, C: (A or B) and (A or C)
    },

    "(A∪B)∩(A∪C)": {
        "nombre": "Distributividad",
        "equivalente": "A∪(B∩C)",
        "variables": 3,
        "f1": lambda A, B, C: (A or B) and (A or C),
        "f2": lambda A, B, C: A or (B and C)
    },

    "A∩X": {
        "nombre": "Elemento neutro",
        "equivalente": "A",
        "variables": 1,
        "f1": lambda A: A and True,
        "f2": lambda A: A
    },

    "A∪∅": {
        "nombre": "Elemento neutro",
        "equivalente": "A",
        "variables": 1,
        "f1": lambda A: A or False,
        "f2": lambda A: A
    },

    "A∩∅": {
        "nombre": "Absorción",
        "equivalente": "∅",
        "variables": 1,
        "f1": lambda A: A and False,
        "f2": lambda A: False
    },

    "A∪X": {
        "nombre": "Absorción",
        "equivalente": "X",
        "variables": 1,
        "f1": lambda A: A or True,
        "f2": lambda A: True
    },

    "A∩A": {
        "nombre": "Idempotencia",
        "equivalente": "A",
        "variables": 1,
        "f1": lambda A: A and A,
        "f2": lambda A: A
    },

    "A∪A": {
        "nombre": "Idempotencia",
        "equivalente": "A",
        "variables": 1,
        "f1": lambda A: A or A,
        "f2": lambda A: A
    },

    "(Aᶜ)ᶜ": {
        "nombre": "Involución",
        "equivalente": "A",
        "variables": 1,
        "f1": lambda A: not (not A),
        "f2": lambda A: A
    },



    "(A∩B)ᶜ": {
        "nombre": "Ley de De Morgan",
        "equivalente": "Aᶜ∪Bᶜ",
        "variables": 2,
        "f1": lambda A, B: not (A and B),
        "f2": lambda A, B: (not A) or (not B)
    },

    "Aᶜ∪Bᶜ": {
        "nombre": "Ley de De Morgan",
        "equivalente": "(A∩B)ᶜ",
        "variables": 2,
        "f1": lambda A, B: (not A) or (not B),
        "f2": lambda A, B: not (A and B)
    },

    "(A∪B)ᶜ": {
        "nombre": "Ley de De Morgan",
        "equivalente": "Aᶜ∩Bᶜ",
        "variables": 2,
        "f1": lambda A, B: not (A or B),
        "f2": lambda A, B: (not A) and (not B)
    },

    "Aᶜ∩Bᶜ": {
        "nombre": "Ley de De Morgan",
        "equivalente": "(A∪B)ᶜ",
        "variables": 2,
        "f1": lambda A, B: (not A) and (not B),
        "f2": lambda A, B: not (A or B)
    },


 
    "A∩Aᶜ": {
        "nombre": "Complemento",
        "equivalente": "∅",
        "variables": 1,
        "f1": lambda A: A and (not A),
        "f2": lambda A: False
    },

    "A∪Aᶜ": {
        "nombre": "Complemento",
        "equivalente": "X",
        "variables": 1,
        "f1": lambda A: A or (not A),
        "f2": lambda A: True
    }
}


print("======================================")
print("   PROPIEDADES DE CONJUNTOS")
print("======================================")

print("""
Símbolos:
∩ = Intersección
∪ = Unión
ᶜ = Complemento
∅ = Conjunto vacío
X = Universo

También puedes usar:
& para ∩
| para ∪
^C para complemento
{} para conjunto vacío

Ejemplos:
A ∩ B
A ∪ B
A ∩ (B ∪ C)
(A ∩ B)ᶜ
A ∪ Aᶜ
""")

entrada = input("Escribe una expresión: ")

expresion = normalizar(entrada)



if expresion in propiedades:

    datos = propiedades[expresion]

    nombre = datos["nombre"]
    equivalente = datos["equivalente"]
    variables = datos["variables"]

    f1 = datos["f1"]
    f2 = datos["f2"]

    print("\n======================================")
    print("Propiedad encontrada:", nombre)
    print("======================================")

    print("\nExpresión ingresada:")
    print(expresion)

    print("\nExpresión equivalente:")
    print(equivalente)

    print("\nPor lo tanto:")

    print(expresion, "=", equivalente)



    if variables == 1:

        print("\nTABLA DE VERDAD\n")

        print(
            f"{'A':<5}"
            f"{expresion:<20}"
            f"{equivalente:<20}"
        )

        print("-" * 45)

        for A in [0, 1]:

            r1 = int(f1(A))
            r2 = int(f2(A))

            print(
                f"{A:<5}"
                f"{r1:<20}"
                f"{r2:<20}"
            )
    elif variables == 2:

        print("\nTABLA DE VERDAD\n")

        print(
            f"{'A':<5}"
            f"{'B':<5}"
            f"{expresion:<20}"
            f"{equivalente:<20}"
        )

        print("-" * 50)

        for A, B in product([0, 1], repeat=2):

            r1 = int(f1(A, B))
            r2 = int(f2(A, B))

            print(
                f"{A:<5}"
                f"{B:<5}"
                f"{r1:<20}"
                f"{r2:<20}"
            )

    elif variables == 3:

        print("\nTABLA DE VERDAD\n")

        print(
            f"{'A':<5}"
            f"{'B':<5}"
            f"{'C':<5}"
            f"{expresion:<25}"
            f"{equivalente:<25}"
        )

        print("-" * 70)

        for A, B, C in product([0, 1], repeat=3):

            r1 = int(f1(A, B, C))
            r2 = int(f2(A, B, C))

            print(
                f"{A:<5}"
                f"{B:<5}"
                f"{C:<5}"
                f"{r1:<25}"
                f"{r2:<25}"
            )


    print("\nLas dos expresiones tienen los mismos resultados.")
    print("Por lo tanto, son equivalentes.")


else:

    print("\nNo se encontró esa propiedad.")

    print("""
Revisa que la expresión esté escrita correctamente.

Ejemplos válidos:

A ∩ B
B ∩ A

A ∪ B
B ∪ A

A ∩ (B ∩ C)
(A ∩ B) ∩ C

A ∪ (B ∪ C)
(A ∪ B) ∪ C

A ∩ (B ∪ C)
(A ∩ B) ∪ (A ∩ C)

A ∪ (B ∩ C)
(A ∪ B) ∩ (A ∪ C)

A ∩ X
A ∪ ∅

A ∩ ∅
A ∪ X

A ∩ A
A ∪ A

(Aᶜ)ᶜ

(A ∩ B)ᶜ
Aᶜ ∪ Bᶜ

(A ∪ B)ᶜ
Aᶜ ∩ Bᶜ

A ∩ Aᶜ
A ∪ Aᶜ
""")