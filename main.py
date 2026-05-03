"""
SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ
Curso: Programación - UNAD
Fase 4 - Prácticas simuladas

Desarrollado por:
Javid Daniel vega iseda

Descripción:
Sistema orientado a objetos para gestión de
clientes, servicios y reservas, implementando:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones
- Logs de eventos

"""
from modelos.cliente import Cliente

from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from modelos.reserva import Reserva

from excepciones.excepciones_personalizadas import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)

from utils.logger import registrar_log


print("\n=== SISTEMA SOFTWARE FJ ===\n")


# ==================================================
# OPERACIÓN 1
# CLIENTE VÁLIDO
# ==================================================

try:

    cliente1 = Cliente(
        "Javid Daniel vega iseda",
        "123456789",
        "javi@gmail.com"
    )

    print(cliente1.mostrar_informacion())

except ErrorCliente as e:

    print(f"Error cliente: {e}")


# ==================================================
# OPERACIÓN 2
# CLIENTE INVÁLIDO
# ==================================================

try:

    cliente2 = Cliente(
        "",
        "ABC123",
        "correo_malo"
    )

    print(cliente2.mostrar_informacion())

except ErrorCliente as e:

    print(f"\nError cliente inválido: {e}")


# ==================================================
# OPERACIÓN 3
# SERVICIO VÁLIDO
# ==================================================

try:

    servicio1 = ReservaSala(
        "Sala Premium",
        50000,
        4
    )

    print("\n")
    print(servicio1.describir_servicio())

except ErrorServicio as e:

    print(f"Error servicio: {e}")


# ==================================================
# OPERACIÓN 4
# SERVICIO INVÁLIDO
# ==================================================

try:

    servicio2 = ReservaSala(
        "Sala Error",
        30000,
        -2
    )

    print(servicio2.describir_servicio())

except ErrorServicio as e:

    print(f"\nError servicio inválido: {e}")


# ==================================================
# OPERACIÓN 5
# ALQUILER VÁLIDO
# ==================================================

try:

    equipo1 = AlquilerEquipo(
        "Laptop Gamer",
        80000,
        3
    )

    print("\n")
    print(equipo1.describir_servicio())

except ErrorServicio as e:

    print(f"Error alquiler: {e}")


# ==================================================
# OPERACIÓN 6
# ALQUILER INVÁLIDO
# ==================================================

try:

    equipo2 = AlquilerEquipo(
        "PC Error",
        60000,
        -5
    )

    print(equipo2.describir_servicio())

except ErrorServicio as e:

    print(f"\nError alquiler inválido: {e}")


# ==================================================
# OPERACIÓN 7
# ASESORÍA VÁLIDA
# ==================================================

try:

    asesoria1 = AsesoriaEspecializada(
        "Asesoría IA",
        100000,
        "avanzada"
    )

    print("\n")
    print(asesoria1.describir_servicio())

except ErrorServicio as e:

    print(f"Error asesoría: {e}")


# ==================================================
# OPERACIÓN 8
# ASESORÍA INVÁLIDA
# ==================================================

try:

    asesoria2 = AsesoriaEspecializada(
        "Asesoría Error",
        50000,
        "experto"
    )

    print(asesoria2.describir_servicio())

except ErrorServicio as e:

    print(f"\nError asesoría inválida: {e}")


# ==================================================
# OPERACIÓN 9
# RESERVA EXITOSA
# ==================================================

try:

    reserva1 = Reserva(
        cliente1,
        servicio1,
        4
    )

    print("\n")
    print(reserva1.mostrar_reserva())

    resultado = reserva1.procesar_reserva()

    print(resultado)

    print(reserva1.mostrar_reserva())

except ErrorReserva as e:

    print(f"Error reserva: {e}")


# ==================================================
# OPERACIÓN 10
# RESERVA FALLIDA
# ==================================================

try:

    reserva2 = Reserva(
        cliente1,
        servicio1,
        -10
    )

    print("\n")
    print(reserva2.mostrar_reserva())

    resultado = reserva2.procesar_reserva()

    print(resultado)

except ErrorReserva as e:

    print(f"\nError reserva inválida: {e}")


# ==================================================
# FINAL
# ==================================================

finally:

    registrar_log("El sistema finalizó correctamente")

    print("\n=== FIN DEL SISTEMA ===")