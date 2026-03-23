import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions import AppError

logger = logging.getLogger("vitory")

STATUS_MAP: dict[str, int] = {
    "NOT_FOUND": 404,
    "CONFLICT": 409,
    "FORBIDDEN": 403,
    "UNAUTHORIZED": 401,
    "VALIDATION_ERROR": 422,
    "BUSINESS_RULE_VIOLATION": 422,
    "EXTERNAL_SERVICE_ERROR": 502,
    "PENDING_VERIFICATION": 409,
    "TOKEN_EXPIRED": 400,
    "TOKEN_INVALID": 400,
    "RATE_LIMITED": 429,
}


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
        status_code = STATUS_MAP.get(exc.code, 500)
        return JSONResponse(
            status_code=status_code,
            content={
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                    "request_id": getattr(request.state, "request_id", "unknown"),
                },
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_error_handler(request: Request, exc: Exception) -> JSONResponse:
        logger.exception(
            "Error no manejado",
            extra={"request_id": getattr(request.state, "request_id", "unknown")},
        )
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "Error interno del servidor",
                    "request_id": getattr(request.state, "request_id", "unknown"),
                },
            },
        )
