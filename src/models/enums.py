"""Enums del dominio de autenticación.

Separados de los modelos ORM para reutilización entre módulos
(schemas, services, handlers) sin acoplar al ORM.
"""

import enum


class Gender(enum.StrEnum):
    MASCULINO = "masculino"
    FEMENINO = "femenino"
    OTRO = "otro"


class UserStatus(enum.StrEnum):
    PENDIENTE_VERIFICACION = "pendiente_verificacion"
    ACTIVO = "activo"
    SUSPENDIDO = "suspendido"
    INACTIVO = "inactivo"


class CredentialType(enum.StrEnum):
    PASSWORD = "password"
    # Futuros: GOOGLE = "google", APPLE = "apple"
