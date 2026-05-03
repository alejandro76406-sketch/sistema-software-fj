# Importación de clases necesarias
from modelos.entidad import Entidad

# Importación de excepción personalizada
from excepciones.excepciones_personalizadas import ErrorCliente

# Importación del sistema de logs
from utils.logger import registrar_log

# Clase Cliente que hereda de Entidad
class Cliente(Entidad):
    def __init__(self, nombre, documento, correo):

        self.__nombre = None
        self.__documento = None
        self.__correo = None

        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_correo(correo)

    # GETTERS
    

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    
    # SETTERS CON VALIDACIONES
   
    # Método setter para validar el nombre
    
    def set_nombre(self, nombre):

        try:

            if not nombre.strip():
                raise ErrorCliente("El nombre no puede estar vacío")

            self.__nombre = nombre
            registrar_log(f"Nombre asignado correctamente: {nombre}")

        except ErrorCliente as e:

            registrar_log(f"ERROR CLIENTE: {e}")
            raise

    def set_documento(self, documento):

        try:

            if not documento.isdigit():
                raise ErrorCliente("El documento debe contener solo números")

            self.__documento = documento
            registrar_log(f"Documento asignado: {documento}")

        except ErrorCliente as e:

            registrar_log(f"ERROR CLIENTE: {e}")
            raise

    def set_correo(self, correo):

        try:

            if "@" not in correo or "." not in correo:
                raise ErrorCliente("Correo electrónico inválido")

            self.__correo = correo
            registrar_log(f"Correo asignado: {correo}")

        except ErrorCliente as e:

            registrar_log(f"ERROR CLIENTE: {e}")
            raise

   
    # MÉTODO ABSTRACTO

    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}"
        )