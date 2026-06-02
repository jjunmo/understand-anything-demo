import uuid
from typing import List

from fastapi import APIRouter

from dependencies.services import BoardServiceDep, BoardServiceTransactionDep
from schemas.board import PostCreate, PostResponse
from schemas.common import SuccessResponse

router = APIRouter(prefix="/posts", tags=["Board"])


@router.post("", response_model=SuccessResponse[PostResponse])
def create_post(data: PostCreate, board_service: BoardServiceTransactionDep):
    post = board_service.create_post(data)
    return SuccessResponse(
        data=PostResponse.model_validate(post), message="게시글이 작성되었습니다"
    )


@router.get("", response_model=SuccessResponse[List[PostResponse]])
def list_posts(board_id: uuid.UUID, board_service: BoardServiceDep):
    posts = board_service.list_posts(board_id)
    return SuccessResponse(data=[PostResponse.model_validate(p) for p in posts])


@router.get("/{post_id}", response_model=SuccessResponse[PostResponse])
def get_post(post_id: uuid.UUID, board_service: BoardServiceTransactionDep):
    post = board_service.get_post(post_id)
    return SuccessResponse(data=PostResponse.model_validate(post))
