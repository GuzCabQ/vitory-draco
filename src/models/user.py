from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel
from src.models.enums import Gender, UserStatus

if TYPE_CHECKING:
    from datetime import date, datetime

    from src.models.credential import Credential
    from src.models.verification_token import VerificationToken


class User(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(100), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name_2: Mapped[str | None] = mapped_column(String(50), nullable=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[Gender] = mapped_column(
        Enum(Gender, name="gender_enum"),
        nullable=False,
    )
    phone: Mapped[str | None] = mapped_column(String(15), nullable=True)
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus, name="user_status_enum"),
        default=UserStatus.PENDIENTE_VERIFICACION,
        server_default=UserStatus.PENDIENTE_VERIFICACION,
        nullable=False,
    )
    accepts_terms_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    email_verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relaciones
    credentials: Mapped[list[Credential]] = relationship(
        "Credential",
        back_populates="user",
        lazy="noload",
    )
    verification_tokens: Mapped[list[VerificationToken]] = relationship(
        "VerificationToken",
        back_populates="user",
        lazy="noload",
    )
