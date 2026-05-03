from excepciones.excepciones_personalizadas import ErrorReserva
from utils.logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # =========================
    # CONFIRMAR RESERVA
    # =========================

    def confirmar_reserva(self):

        try:

            if self.duracion <= 0:
                raise ErrorReserva(
                    "La duración debe ser mayor a cero"
                )

            self.estado = "Confirmada"

            registrar_log(
                f"Reserva confirmada para "
                f"{self.cliente.get_nombre()}"
            )

            return "Reserva confirmada correctamente"

        except ErrorReserva as e:

            registrar_log(f"ERROR RESERVA: {e}")
            raise

    # =========================
    # CANCELAR RESERVA
    # =========================

    def cancelar_reserva(self):

        try:

            if self.estado == "Cancelada":
                raise ErrorReserva(
                    "La reserva ya estaba cancelada"
                )

            self.estado = "Cancelada"

            registrar_log(
                f"Reserva cancelada para "
                f"{self.cliente.get_nombre()}"
            )

            return "Reserva cancelada correctamente"

        except ErrorReserva as e:

            registrar_log(f"ERROR CANCELACIÓN: {e}")
            raise

    # =========================
    # PROCESAR RESERVA
    # =========================

    def procesar_reserva(self):

        try:

            mensaje = self.confirmar_reserva()

        except ErrorReserva as e:

            raise ErrorReserva(
                "Error al procesar la reserva"
            ) from e

        else:

            registrar_log(
                "Procesamiento realizado correctamente"
            )

            return mensaje

        finally:

            registrar_log(
                "Finalizó intento de procesamiento"
            )

    # =========================
    # MOSTRAR INFORMACIÓN
    # =========================

    def mostrar_reserva(self):

        return (
            f"\n===== RESERVA =====\n"
            f"Cliente: {self.cliente.get_nombre()}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Estado: {self.estado}\n"
            f"Duración: {self.duracion}"
        )