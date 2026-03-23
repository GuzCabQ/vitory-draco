# CLAUDE.md — vitory-draco

Backend API de VITORY (GestDeport). Gestion de Torneos de Tocho Bandera.

## Stack
- Python 3.12 + FastAPI + Pydantic v2
- SQLAlchemy 2.0 (async) + Alembic + PostgreSQL 16
- passlib[bcrypt] + python-jose (JWT)
- Resend (email)
- pytest + pytest-asyncio + httpx (tests)
- ruff (linter + formatter)

## Comandos
- `uvicorn src.main:app --reload` — servidor de desarrollo
- `ruff check .` — lint
- `ruff format .` — formatter
- `pytest` — ejecutar tests
- `alembic upgrade head` — aplicar migraciones
- `alembic revision --autogenerate -m "desc"` — generar migracion

## Arquitectura: 4 capas
Handler (router) → Schema (Pydantic) → Service (logica) → Repository (BD)

## Reglas
- Logica de negocio SOLO en services, nunca en handlers
- Excepciones de dominio (AppError), nunca HTTPException en services
- Repositories usan flush(), nunca commit() (get_db maneja commit)
- SQLAlchemy 2.0: select() siempre, session.query() nunca
- Soft delete con deleted_at (BaseModel)
- Todos los campos tipo Mapped + mapped_column

## Estandares
- Ver ET-009 y ET-010 en el repo VITORY (docs/)
