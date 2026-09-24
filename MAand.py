from itertools import product
print("&   = AND")
print("|   = OR")
print("~   = NOT")
print("<-> = BICONDICIONAL")
print()

propiedades = {

    "p&q": ("Conmutatividad", "q&p"),
    "q&p": ("Conmutatividad", "p&q"),

    "p|q": ("Conmutatividad", "q|p"),
    "q|p": ("Conmutatividad", "p|q"),

    "p&(q&r)": ("Asociatividad", "(p&q)&r"),
    "(p&q)&r": ("Asociatividad", "p&(q&r)"),

    "p|(q|r)": ("Asociatividad", "(p|q)|r"),
    "(p|q)|r": ("Asociatividad", "p|(q|r)"),

    "p&(q|r)": ("Distributividad", "(p&q)|(p&r)"),
    "(p&q)|(p&r)": ("Distributividad", "p&(q|r)"),

    "p|(q&r)": ("Distributividad", "(p|q)&(p|r)"),
    "(p|q)&(p|r)": ("Distributividad", "p|(q&r)"),

    "p&1": ("Elemento neutro", "p"),
    "p|0": ("Elemento neutro", "p"),

    "p&0": ("Absorción", "0"),
    "p|1": ("Absorción", "1"),

    "p&p": ("Idempotencia", "p"),
    "p|p": ("Idempotencia", "p"),

    "~~p": ("Involución", "p"),

    "~(p&q)": ("Ley de De Morgan", "~p|~q"),
    "~p|~q": ("Ley de De Morgan", "~(p&q)"),

    "~(p|q)": ("Ley de De Morgan", "~p&~q"),
    "~p&~q": ("Ley de De Morgan", "~(p|q)"),

    "p&~p": ("Complemento", "0"),
    "p|~p": ("Tercero excluido", "1"),


    "p<->q": ("Bicondicional", "(p&q)|(~p&~q)"),
    "q<->p": ("Bicondicional", "(q&p)|(~q&~p)")
}

def evaluar(expresion, p, q, r):

    if expresion == "0":
        return False

    if expresion == "1":
        return True

    if expresion == "p<->q":
        return p == q

    if expresion == "q<->p":
        return q == p

    return eval(
        expresion,
        {"__builtins__": {}},
        {
            "p": p,
            "q": q,
            "r": r
        }
    )



expresion = input("Ingresa una expresión lógica: ")

# Eliminar espacios
expresion = expresion.replace(" ", "")


if expresion in propiedades:

    propiedad, equivalente = propiedades[expresion]


    print("Propiedad:", propiedad)
    print("Expresión original:", expresion)
    print("Expresión equivalente:", equivalente)

    variables = []

    for variable in ["p", "q", "r"]:

        if variable in expresion or variable in equivalente:
            variables.append(variable)


    print("TABLA DE VERDAD")

    for variable in variables:
        print(variable, end="\t")

    print(expresion, end="\t")
    print(equivalente)


    combinaciones = product(
        [True, False],
        repeat=len(variables)
    )

    son_equivalentes = True

    for combinacion in combinaciones:

        valores = {
            "p": False,
            "q": False,
            "r": False
        }

        for i in range(len(variables)):
            valores[variables[i]] = combinacion[i]


        resultado1 = evaluar(
            expresion,
            valores["p"],
            valores["q"],
            valores["r"]
        )

        resultado2 = evaluar(
            equivalente,
            valores["p"],
            valores["q"],
            valores["r"]
        )

        for valor in combinacion:
            print(int(valor), end="\t")


        print(
            int(resultado1),
            "\t",
            int(resultado2)
        )

        if resultado1 != resultado2:
            son_equivalentes = False

    if son_equivalentes:
        print("Las expresiones SON equivalentes.")
    else:
        print("Las expresiones NO son equivalentes.")

else:

    print("\nLa expresión ingresada no está registrada.")