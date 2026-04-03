from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.enums import CredentialType

if TYPE_CHECKING:
    from datetime import datetime

    from src.models.user import User


class Credential(Base):
    """Credenciales de autenticacion separadas del perfil de usuario.
    Sigue patron de la industria (DT-004): aislamiento de credenciales."""

    __tablename__ = "credentials"
    __table_args__ = (
        UniqueConstraint("user_id", "credential_type", name="uq_credentials_user_type"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    credential_type: Mapped[CredentialType] = mapped_column(
        Enum(CredentialType, name="credential_type_enum"),
        nullable=False,
    )
    credential_hash: Mapped[str] = mapped_column(String(512), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    last_used_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relacion
    user: Mapped[User] = relationship("User", back_populates="credentials", lazy="noload")
