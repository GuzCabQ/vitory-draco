class AppError(Exception):
    """Base para todas las excepciones de dominio de VITORY."""

    def __init__(self, message: str, code: str = "APP_ERROR") -> None:
        self.message = message
        self.code = code
        super().__init__(message)


class NotFoundError(AppError):
    def __init__(self, resource: str, identifier: str) -> None:
        super().__init__(
            message=f"{resource} con identificador '{identifier}' no encontrado",
            code="NOT_FOUND",
        )


class ConflictError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(message=message, code="CONFLICT")


class BusinessRuleError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(message=message, code="BUSINESS_RULE_VIOLATION")


class ForbiddenError(AppError):
    def __init__(self, message: str = "No tiene permisos para esta operacion") -> None:
        super().__init__(message=message, code="FORBIDDEN")


class UnauthorizedError(AppError):
    def __init__(self, message: str = "No autenticado") -> None:
        super().__init__(message=message, code="UNAUTHORIZED")


class ValidationError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(message=message, code="VALIDATION_ERROR")


class ExternalServiceError(AppError):
    def __init__(self, service: str, message: str) -> None:
        super().__init__(
            message=f"Error en servicio externo '{service}': {message}",
            code="EXTERNAL_SERVICE_ERROR",
        )
