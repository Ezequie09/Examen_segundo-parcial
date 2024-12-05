
# Clase primarioa, usando encapsulamiento
class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_info(self):
        return f"Libro: {self.__titulo}, Autor: {self.__autor}"

# Clase secundaria usando herencia
class Available_Books(Libro):
    def __init__(self, titulo, autor, copias):
        super().__init__(titulo, autor)
        self.__copias = copias

    def prestar_libro(self):
        if self.__copias > 0:
            self.__copias -= 1
            return "Libro prestado exitosamente."
        else:
            raise Exception("No hay copias disponibles.")

# Uso de polimorfismo
class Catalogue:
    def mostrar(self, libro):
        return libro.get_info()

# Uso de errores con try-catch
try:
    libro = Available_Books("El Principito", "Antoine de Saint-Exupéry", 2)
    print(libro.prestar_libro())
    print(libro.prestar_libro())
    print(libro.prestar_libro())  # Esto lanzará una excepción
except Exception as e:
    print(f"Error: {e}")