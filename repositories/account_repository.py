from typing import Optional

from sqlalchemy.orm import Session

from models.account import Account
from repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository[Account]):
    def __init__(self, db: Session):
        super().__init__(Account, db)

    def get_by_user_id(self, user_id: str) -> Optional[Account]:
        """로그인 ID로 계정을 조회한다."""
        return self.filter_by_one(user_id=user_id)
