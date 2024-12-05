class User:
    # Encapsulamiento: atributos privados
    def __init__(self, celular, edad, cuenta):
        self.__celular = celular
        self.__edad = edad
        self.__cuenta = cuenta

    # Métodos de acceso para encapsulamiento
    def get_cuenta(self):
        return self.__cuenta

    def set_cuenta(self, cuenta):
        self.__cuenta = cuenta

    def search_author(self, author):
        print(f"Buscando libros del autor: {author}")

    def check_availability(self, book):
        print(f"Verificando disponibilidad del libro: {book}")


class Catalogue:
    def __init__(self, sections):
        self.sections = sections

    def check_available(self, book):
        # Simulación de verificación de disponibilidad
        print(f"El libro '{book}' está disponible.")


class Book:
    # Encapsulamiento: atributos privados
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo

    # Métodos de acceso para encapsulamiento
    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def check_code(self):
        print(f"Código del libro: {self.__codigo}")


# Herencia: Loan hereda de User
class Loan(User):
    def __init__(self, celular, edad, cuenta, libro, estado):
        super().__init__(celular, edad, cuenta)  # Llamada al constructor de la clase padre
        self.libro = libro
        self.estado = estado

    # Polimorfismo: redefinición del método check_availability
    def check_availability(self, book):
        print(f"Chequeando disponibilidad específicamente para préstamo del libro: {book}")

    def check_permissions(self):
        print("Verificando permisos del usuario para el préstamo.")

    def update_account(self):
        print("Actualizando cuenta del usuario después del préstamo.")


# Manejo de errores (Try-Catch)
def process_loan():
    try:
        # Solicitar datos del usuario
        celular = input("Introduce tu número de celular: ")
        edad = int(input("Introduce tu edad: "))
        cuenta = input("Introduce tu nombre de cuenta: ")

        # Solicitar datos del libro
        nombre_libro = input("Introduce el nombre del libro que quieres pedir prestado: ")
        codigo_libro = input("Introduce el código del libro: ")

        # Crear instancias
        usuario = Loan(celular, edad, cuenta, nombre_libro, "En curso")
        libro = Book(nombre_libro, codigo_libro)
        catalogue = Catalogue(["Ficción", "No ficción", "Ciencia"])

        # Simular flujo de préstamo
        usuario.search_author(input("Introduce el nombre de un autor para buscar: "))
        usuario.check_availability(nombre_libro)
        catalogue.check_available(nombre_libro)
        libro.check_code()
        usuario.check_permissions()
        usuario.update_account()

        print("¡Préstamo completado con éxito!")

    except Exception as e:  # Manejo de cualquier excepción
        print(f"Ocurrió un error en el proceso de préstamo: {e}")


# Llamada al proceso de préstamo
process_loan()