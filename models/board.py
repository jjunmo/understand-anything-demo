import uuid
from enum import Enum

from sqlalchemy import ForeignKey, Integer, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin


class BoardType(str, Enum):
    NOTICE = "NOTICE"
    FREE = "FREE"
    REVIEW = "REVIEW"


class Board(Base, TimestampMixin):
    """게시판 엔티티"""

    __tablename__ = "boards"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    board_type: Mapped[BoardType] = mapped_column(
        String(20), default=BoardType.FREE, nullable=False
    )


class Post(Base, TimestampMixin):
    """게시글 엔티티 — author_id로 Account와 연결된다."""

    __tablename__ = "posts"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    board_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("boards.id"), nullable=False
    )
    author_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("accounts.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    view_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    like_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
