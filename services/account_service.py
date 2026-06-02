import uuid

from loguru import logger

from exceptions.common import ServiceException
from models.account import Account
from repositories.account_repository import AccountRepository
from schemas.account import AccountCreate, AccountLogin
from util.security import hash_password, verify_password


class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    def signup(self, data: AccountCreate) -> Account:
        """회원가입 — 중복 ID 검증 후 비밀번호를 해싱해 저장한다."""
        if self.account_repo.get_by_user_id(data.user_id):
            raise ServiceException.conflict("이미 사용 중인 아이디입니다")

        account = Account(
            user_id=data.user_id,
            user_pw=hash_password(data.user_pw),
            name=data.name,
            phone=data.phone,
            email=data.email,
        )
        created = self.account_repo.create(account)
        logger.info("회원가입 완료: {}", created.user_id)
        return created

    def login(self, data: AccountLogin) -> Account:
        """로그인 — 아이디 조회 후 비밀번호를 검증한다."""
        account = self.account_repo.get_by_user_id(data.user_id)
        if not account or not verify_password(data.user_pw, account.user_pw):
            raise ServiceException.unauthorized("아이디 또는 비밀번호가 올바르지 않습니다")
        logger.info("로그인 성공: {}", account.user_id)
        return account

    def get_account(self, account_id: uuid.UUID) -> Account:
        """계정 정보 조회."""
        account = self.account_repo.get_by_id(account_id)
        if not account:
            raise ServiceException.not_found("계정을 찾을 수 없습니다")
        return account
