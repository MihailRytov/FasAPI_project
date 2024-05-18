"""
Создаем базовый класс, от него буду наследоваться все
остальные классы (таблицы) нашей базы данных.
"""

from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import Column, BIGINT


class Base(DeclarativeBase):
    """
    Нам не нужно чтобы эта таблица создавалась в наше БД
    Для этого указываем __abstract__ = True
    """

    __abstract__ = True

    """
    Автоматически генерируем имя таблицы.
    Переводим в нижний регистр, и добавлем множественное число.
    Через атрибут префикс можно добавить префикс.
    """

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(BIGINT, primary_key=True)
