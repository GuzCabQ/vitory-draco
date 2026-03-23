from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base de datos
    database_url: str = "postgresql+asyncpg://vitory:password@localhost:5432/vitory"
    test_database_url: str = "postgresql+asyncpg://vitory:password@localhost:5432/vitory_test"

    # Seguridad
    jwt_secret: str = "cambiar-en-produccion"
    jwt_refresh_secret: str = "otro-secreto-diferente"

    # Email
    resend_api_key: str = ""
    email_from: str = "noreply@vitory.app"
    email_from_name: str = "VITORY"

    # Verificacion
    verification_url_base: str = "http://localhost:8000/api/v1/auth/verify"
    verification_token_expiry_hours: int = 24
    resend_max_per_hour: int = 3

    # Server
    debug: bool = True
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8080"]

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
