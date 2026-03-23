import uuid
from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.base import BaseModel


class BaseRepository[T: BaseModel]:
    def __init__(self, model: type[T], session: AsyncSession) -> None:
        self._model = model
        self._session = session

    async def get_by_id(self, entity_id: uuid.UUID) -> T | None:
        stmt = select(self._model).where(
            self._model.id == entity_id,
            self._model.deleted_at.is_(None),
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, **kwargs) -> T:
        entity = self._model(**kwargs)
        self._session.add(entity)
        await self._session.flush()
        return entity

    async def update(self, entity: T, **kwargs) -> T:
        for key, value in kwargs.items():
            setattr(entity, key, value)
        await self._session.flush()
        return entity

    async def delete(self, entity_id: uuid.UUID) -> None:
        entity = await self.get_by_id(entity_id)
        if entity:
            entity.deleted_at = datetime.now(UTC)
            await self._session.flush()

    async def count(self) -> int:
        stmt = (
            select(func.count()).select_from(self._model).where(self._model.deleted_at.is_(None))
        )
        result = await self._session.execute(stmt)
        return result.scalar_one()
