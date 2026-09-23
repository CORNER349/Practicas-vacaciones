# --- LA PLANTILLA (CLASE) ---
class CuentaBancaria:
    # El método __init__ asigna los atributos (datos) cuando se crea la cuenta
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial  # Atributo

    # Métodos (Acciones que la cuenta sabe hacer)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depositado: ${cantidad}. Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retirado: ${cantidad}. Saldo restante: ${self.saldo}")
        else:
            print("¡Fondos insuficientes o cantidad inválida!")


# --- CREACIÓN DE OBJETOS ---
# Creamos una "instancia" (un objeto real a partir del plano)
cuenta_carlos = CuentaBancaria("Carlos", 500.0)

# Usamos los métodos del objeto
cuenta_carlos.depositar(200.0)
cuenta_carlos.retirar(100.0)

# ¡Y crear una segunda cuenta es inmediato!
cuenta_ana = CuentaBancaria("Ana", 1200.0)
cuenta_ana.retirar(300.0)