import uuid

from fastapi import APIRouter

from dependencies.services import AccountServiceDep, AccountServiceTransactionDep
from schemas.account import AccountCreate, AccountLogin, AccountResponse
from schemas.common import SuccessResponse

router = APIRouter(prefix="/accounts", tags=["Account"])


@router.post("/signup", response_model=SuccessResponse[AccountResponse])
def signup(data: AccountCreate, account_service: AccountServiceTransactionDep):
    account = account_service.signup(data)
    return SuccessResponse(
        data=AccountResponse.model_validate(account), message="회원가입이 완료되었습니다"
    )


@router.post("/login", response_model=SuccessResponse[AccountResponse])
def login(data: AccountLogin, account_service: AccountServiceTransactionDep):
    account = account_service.login(data)
    return SuccessResponse(
        data=AccountResponse.model_validate(account), message="로그인되었습니다"
    )


@router.get("/{account_id}", response_model=SuccessResponse[AccountResponse])
def get_account(account_id: uuid.UUID, account_service: AccountServiceDep):
    account = account_service.get_account(account_id)
    return SuccessResponse(data=AccountResponse.model_validate(account))
