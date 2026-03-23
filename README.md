# vitory-draco

> Backend API de VITORY — Plataforma de Gestion de Torneos de Tocho Bandera

## Stack

- Python 3.12
- FastAPI + Pydantic v2
- SQLAlchemy 2.0 (async) + Alembic
- PostgreSQL 16

## Setup

### Prerequisitos

- Python 3.12+
- PostgreSQL 16
- Git
- uv (gestor de paquetes)

### Instalacion

1. Clonar el repo:
   ```bash
   git clone git@github.com:GuzCabQ/vitory-draco.git
   cd vitory-draco
   ```

2. Crear entorno virtual:
   ```bash
   uv venv --python 3.12
   source .venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   uv pip install -e ".[dev]"
   ```

4. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   # Editar .env con tus valores locales
   ```

5. Crear bases de datos:
   ```bash
   psql postgres -c "CREATE USER vitory WITH PASSWORD 'vitory_dev_2026';"
   psql postgres -c "CREATE DATABASE vitory OWNER vitory;"
   psql postgres -c "CREATE DATABASE vitory_test OWNER vitory;"
   ```

6. Ejecutar migraciones:
   ```bash
   alembic upgrade head
   ```

7. Iniciar servidor:
   ```bash
   uvicorn src.main:app --reload
   ```

8. Verificar: abrir http://localhost:8000/api/health

## Comandos utiles

| Comando | Descripcion |
|---------|-------------|
| `uvicorn src.main:app --reload` | Dev server |
| `ruff check .` | Lint |
| `ruff format .` | Format |
| `pytest` | Tests |
| `alembic upgrade head` | Migraciones |
| `alembic revision --autogenerate -m "desc"` | Nueva migracion |

## Documentacion

- Swagger: http://localhost:8000/docs
- Specs y User Stories: ver repo [VITORY](https://github.com/GuzCabQ/VITORY)
