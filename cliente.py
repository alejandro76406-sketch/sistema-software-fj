import re
import datetime

# Excepción personalizada para clientes inválidos
class ClienteInvalidoError(Exception):
    pass

# Función para registrar errores y eventos en logs.txt
def log_event(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

class Cliente:
    def __init__(self, nombre, correo, telefono):
        try:
            self.__set_nombre(nombre)
            self.__set_correo(correo)
            self.__set_telefono(telefono)
            log_event(f"Cliente creado: {self.__nombre}, {self.__correo}, {self.__telefono}")
        except ClienteInvalidoError as e:
            log_event(f"Error al crear cliente: {str(e)}")
            raise

    # Encapsulación con getters y setters
    def __set_nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 3:
            raise ClienteInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = nombre.strip()

    def __set_correo(self, correo):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron, correo):
            raise ClienteInvalidoError("Correo electrónico inválido.")
        self.__correo = correo

    def __set_telefono(self, telefono):
        if not telefono.isdigit() or len(telefono) < 7:
            raise ClienteInvalidoError("El teléfono debe contener solo números y al menos 7 dígitos.")
        self.__telefono = telefono

    # Métodos públicos para acceder a los datos
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Método para actualizar datos con manejo de errores
    def actualizar_datos(self, nombre=None, correo=None, telefono=None):
        try:
            if nombre:
                self.__set_nombre(nombre)
            if correo:
                self.__set_correo(correo)
            if telefono:
                self.__set_telefono(telefono)
            log_event(f"Datos actualizados para cliente: {self.__nombre}")
        except ClienteInvalidoError as e:
            log_event(f"Error al actualizar cliente: {str(e)}")
            raise

# Ejemplo de uso y prueba de errores
if __name__ == "__main__":
    try:
        cliente1 = Cliente("Alejandro", "alejandro@example.com", "3001234567")
        print("Cliente creado:", cliente1.get_nombre(), cliente1.get_correo(), cliente1.get_telefono())

        # Intento inválido
        cliente2 = Cliente("Al", "correo_invalido", "123")
    except Exception as e:
        print("Se manejó un error:", e)
