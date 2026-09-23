from itertools import product

print("==========================================")
print("   PROPIEDADES DE LÓGICA PROPOSICIONAL")
print("==========================================")
print("&   = AND")
print("|   = OR")
print("~   = NOT")
print("<-> = BICONDICIONAL")
print()


# ==========================================================
# PROPIEDADES DE LÓGICA PROPOSICIONAL
# ==========================================================

propiedades = {

    # 1. CONMUTATIVIDAD
    "p&q": ("Conmutatividad", "q&p"),
    "q&p": ("Conmutatividad", "p&q"),

    "p|q": ("Conmutatividad", "q|p"),
    "q|p": ("Conmutatividad", "p|q"),


    # 2. ASOCIATIVIDAD
    "p&(q&r)": ("Asociatividad", "(p&q)&r"),
    "(p&q)&r": ("Asociatividad", "p&(q&r)"),

    "p|(q|r)": ("Asociatividad", "(p|q)|r"),
    "(p|q)|r": ("Asociatividad", "p|(q|r)"),


    # 3. DISTRIBUTIVIDAD
    "p&(q|r)": ("Distributividad", "(p&q)|(p&r)"),
    "(p&q)|(p&r)": ("Distributividad", "p&(q|r)"),

    "p|(q&r)": ("Distributividad", "(p|q)&(p|r)"),
    "(p|q)&(p|r)": ("Distributividad", "p|(q&r)"),


    # 4. ELEMENTOS NEUTROS
    "p&1": ("Elemento neutro", "p"),
    "p|0": ("Elemento neutro", "p"),


    # 5. ABSORCIÓN
    "p&0": ("Absorción", "0"),
    "p|1": ("Absorción", "1"),


    # 6. IDEMPOTENCIA
    "p&p": ("Idempotencia", "p"),
    "p|p": ("Idempotencia", "p"),


    # 7. INVOLUCIÓN
    "~~p": ("Involución", "p"),


    # 8. LEYES DE DE MORGAN
    "~(p&q)": ("Ley de De Morgan", "~p|~q"),
    "~p|~q": ("Ley de De Morgan", "~(p&q)"),

    "~(p|q)": ("Ley de De Morgan", "~p&~q"),
    "~p&~q": ("Ley de De Morgan", "~(p|q)"),


    # 9. COMPLEMENTO / TERCERO EXCLUIDO
    "p&~p": ("Complemento", "0"),
    "p|~p": ("Tercero excluido", "1"),


    # 10. BICONDICIONAL
    "p<->q": ("Bicondicional", "(p&q)|(~p&~q)"),
    "q<->p": ("Bicondicional", "(q&p)|(~q&~p)")
}


# ==========================================================
# FUNCIÓN PARA EVALUAR UNA EXPRESIÓN
# ==========================================================

def evaluar(expresion, p, q, r):

    # Constantes
    if expresion == "0":
        return False

    if expresion == "1":
        return True

    # Bicondicional
    if expresion == "p<->q":
        return p == q

    if expresion == "q<->p":
        return q == p

    # Evaluar las demás expresiones
    return eval(
        expresion,
        {"__builtins__": {}},
        {
            "p": p,
            "q": q,
            "r": r
        }
    )


# ==========================================================
# PEDIR EXPRESIÓN AL USUARIO
# ==========================================================

expresion = input("Ingresa una expresión lógica: ")

# Eliminar espacios
expresion = expresion.replace(" ", "")


# ==========================================================
# BUSCAR LA PROPIEDAD
# ==========================================================

if expresion in propiedades:

    propiedad, equivalente = propiedades[expresion]

    print("\n==========================================")
    print("RESULTADO")
    print("==========================================")

    print("Propiedad:", propiedad)
    print("Expresión original:", expresion)
    print("Expresión equivalente:", equivalente)


    # ======================================================
    # DETECTAR LAS VARIABLES
    # ======================================================

    variables = []

    for variable in ["p", "q", "r"]:

        if variable in expresion or variable in equivalente:
            variables.append(variable)


    # ======================================================
    # TABLA DE VERDAD
    # ======================================================

    print("\n==========================================")
    print("TABLA DE VERDAD")
    print("==========================================\n")

    # Encabezados
    for variable in variables:
        print(variable, end="\t")

    print(expresion, end="\t")
    print(equivalente)


    # ======================================================
    # GENERAR COMBINACIONES
    # ======================================================

    combinaciones = product(
        [True, False],
        repeat=len(variables)
    )


    # ======================================================
    # EVALUAR CADA COMBINACIÓN
    # ======================================================

    son_equivalentes = True

    for combinacion in combinaciones:

        valores = {
            "p": False,
            "q": False,
            "r": False
        }

        # Asignar valores a las variables
        for i in range(len(variables)):
            valores[variables[i]] = combinacion[i]


        # Evaluar expresión original
        resultado1 = evaluar(
            expresion,
            valores["p"],
            valores["q"],
            valores["r"]
        )


        # Evaluar expresión equivalente
        resultado2 = evaluar(
            equivalente,
            valores["p"],
            valores["q"],
            valores["r"]
        )


        # Mostrar valores de las variables
        for valor in combinacion:
            print(int(valor), end="\t")


        # Mostrar resultados
        print(
            int(resultado1),
            "\t",
            int(resultado2)
        )


        # Comprobar equivalencia
        if resultado1 != resultado2:
            son_equivalentes = False


    # ======================================================
    # RESULTADO FINAL
    # ======================================================

    print("\n==========================================")

    if son_equivalentes:
        print("Las expresiones SON equivalentes.")
    else:
        print("Las expresiones NO son equivalentes.")

    print("==========================================")


else:

    print("\nLa expresión ingresada no está registrada.")