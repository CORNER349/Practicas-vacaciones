# --- CLASE 1: LIBRO ---
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"✅ Has tomado prestado '{self.titulo}'.")
        else:
            print(f"⚠️ El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"✅ Has devuelto '{self.titulo}'.")
        else:
            print(f"⚠️ El libro '{self.titulo}' no estaba prestado.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"📖 '{self.titulo}' - {self.autor} [{estado}]")


# --- CLASE 2: BIBLIOTECA ---
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Lista vacía para almacenar objetos de la clase Libro

    def agregar_libro(self, libro):
        # Guardamos el objeto entero dentro de la lista
        self.libros.append(libro)
        print(f"➕ Libro '{libro.titulo}' añadido a la biblioteca '{self.nombre}'.")

    def mostrar_catalogo(self):
        print(f"\n--- Catálogo de la Biblioteca: {self.nombre} ---")
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            # Recorremos la lista de objetos y llamamos al método de cada Libro
            for libro in self.libros:
                libro.mostrar_info()
        print("-------------------------------------------\n")

    def buscar_y_prestar(self, titulo_buscado):
        # Buscamos si existe el libro dentro del catálogo
        encontrado = False
        for libro in self.libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                libro.prestar()  # Ejecuta el método prestar() de ese libro específico
                encontrado = True
                break
        
        if not encontrado:
            print(f"❌ Lo sentimos, no tenemos el libro '{titulo_buscado}' en el catálogo.")
# 1. Creamos la biblioteca
mi_biblioteca = Biblioteca("Biblioteca Central")

# 2. Creamos varios objetos de tipo Libro por separado
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro3 = Libro("1984", "George Orwell")

# 3. Agregamos los libros a la biblioteca
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)
mi_biblioteca.agregar_libro(libro3)

# 4. Ver el catálogo completo
mi_biblioteca.mostrar_catalogo()

# 5. Buscar y prestar un libro a través de la biblioteca
mi_biblioteca.buscar_y_prestar("El Principito")

# 6. Intentar prestarlo de nuevo para verificar la lógica
mi_biblioteca.buscar_y_prestar("El Principito")

# 7. Ver cómo el catálogo se actualizó automáticamente
mi_biblioteca.mostrar_catalogo()