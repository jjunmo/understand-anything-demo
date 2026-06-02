import uuid
from typing import List

from loguru import logger

from exceptions.common import ServiceException
from models.board import Post
from repositories.account_repository import AccountRepository
from repositories.post_repository import PostRepository
from schemas.board import PostCreate


class BoardService:
    def __init__(self, post_repo: PostRepository, account_repo: AccountRepository):
        self.post_repo = post_repo
        self.account_repo = account_repo

    def create_post(self, data: PostCreate) -> Post:
        """게시글 작성 — 작성자 존재 여부를 검증한다."""
        if not self.account_repo.get_by_id(data.author_id):
            raise ServiceException.not_found("작성자 계정을 찾을 수 없습니다")

        post = Post(
            board_id=data.board_id,
            author_id=data.author_id,
            title=data.title,
            content=data.content,
        )
        created = self.post_repo.create(post)
        logger.info("게시글 작성 완료: {}", created.id)
        return created

    def list_posts(self, board_id: uuid.UUID) -> List[Post]:
        """게시판별 게시글 목록 조회."""
        return self.post_repo.list_by_board(board_id)

    def get_post(self, post_id: uuid.UUID) -> Post:
        """게시글 단건 조회 — 조회수를 증가시킨다."""
        post = self.post_repo.get_by_id(post_id)
        if not post:
            raise ServiceException.not_found("게시글을 찾을 수 없습니다")
        post.view_count += 1
        return self.post_repo.update(post)
