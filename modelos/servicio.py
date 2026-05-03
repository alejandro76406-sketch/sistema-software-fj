from abc import ABC, abstractmethod
from excepciones.excepciones_personalizadas import ErrorServicio
from utils.logger import registrar_log


class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, horas):

        super().__init__(nombre, costo_base)

        if horas <= 0:
            registrar_log("ERROR: horas inválidas para sala")
            raise ErrorServicio("Las horas deben ser mayores a cero")

        self.horas = horas

    def calcular_costo(self):

        return self.costo_base * self.horas

    def describir_servicio(self):

        return (
            f"Servicio: Reserva de Sala\n"
            f"Horas: {self.horas}\n"
            f"Costo: {self.calcular_costo()}"
        )
        

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, dias):

        super().__init__(nombre, costo_base)

        if dias <= 0:
            registrar_log("ERROR: días inválidos")
            raise ErrorServicio("Los días deben ser mayores a cero")

        self.dias = dias

    def calcular_costo(self):

        return self.costo_base * self.dias

    def describir_servicio(self):

        return (
            f"Servicio: Alquiler de Equipo\n"
            f"Días: {self.dias}\n"
            f"Costo: {self.calcular_costo()}"
        )
        

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, costo_base, nivel):

        super().__init__(nombre, costo_base)

        niveles_validos = ["basica", "intermedia", "avanzada"]

        if nivel.lower() not in niveles_validos:
            registrar_log("ERROR: nivel inválido")
            raise ErrorServicio("Nivel de asesoría inválido")

        self.nivel = nivel.lower()

    def calcular_costo(self):

        if self.nivel == "basica":
            return self.costo_base

        elif self.nivel == "intermedia":
            return self.costo_base * 1.5

        else:
            return self.costo_base * 2

    def describir_servicio(self):

        return (
            f"Servicio: Asesoría Especializada\n"
            f"Nivel: {self.nivel}\n"
            f"Costo: {self.calcular_costo()}"
        )