import uuid
from typing import List

from sqlalchemy.orm import Session

from models.board import Post
from repositories.base_repository import BaseRepository


class PostRepository(BaseRepository[Post]):
    def __init__(self, db: Session):
        super().__init__(Post, db)

    def list_by_board(self, board_id: uuid.UUID) -> List[Post]:
        """특정 게시판의 게시글 목록을 조회한다."""
        return self.filter_by(board_id=board_id)
