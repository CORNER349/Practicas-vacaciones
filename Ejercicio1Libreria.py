class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Por defecto siempre está disponible al crearse

    def prestar(self):
        if self.disponible == True:
            print("Libro Prestado")
            self.disponible=False
        else:
            print("El libro no esta disponible")
            

    def devolver(self):
        if self.disponible == False:
            print("Libro devuelto")
            self.disponible=True
            estado="Disnopinle"
        else:
            print("No hay nada que devolver")
            Estado="Prestado"
        

    def mostrar_info(self):
        if self.disponible == True:
            print("Libro disponible")
        else:
            print("Libro prestado")
        print(f"Libro: '{self.titulo}' Autor: {self.autor} Estado: {self.estado}")
        

# --- CASO DE PRUEBA PARA VALIDAR TU CÓDIGO ---
# Crea tu objeto
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez")

mi_libro.mostrar_info()  # Debería mostrar que está disponible
mi_libro.prestar()       # Debería prestarlo con éxito
mi_libro.prestar()       # Debería decir que YA está prestado
mi_libro.mostrar_info()  # Debería mostrar que está prestado
mi_libro.devolver()      # Debería devolverlo con éxito