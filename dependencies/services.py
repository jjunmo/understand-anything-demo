"""
Service DI 등록
================
도메인별 Service를 추가할 때 아래 패턴을 따른다.

Sync 예시:
    from typing import Annotated
    from fastapi import Depends
    from dependencies.repositories import TaskRepoDep, TaskRepoTransactionDep
    from services.task_service import TaskService

    def get_task_service_read_only(task_repo: TaskRepoDep) -> TaskService:
        return TaskService(task_repo=task_repo)

    def get_task_service_transactional(task_repo: TaskRepoTransactionDep) -> TaskService:
        return TaskService(task_repo=task_repo)

    TaskServiceDep = Annotated[TaskService, Depends(get_task_service_read_only)]
    TaskServiceTransactionDep = Annotated[TaskService, Depends(get_task_service_transactional)]

Async 예시:
    from typing import Annotated
    from fastapi import Depends
    from dependencies.repositories import TaskAsyncRepoDep, TaskAsyncRepoTransactionDep
    from services.task_async_service import TaskAsyncService

    def get_task_async_service_read_only(
        task_repo: TaskAsyncRepoDep,
    ) -> TaskAsyncService:
        return TaskAsyncService(task_repo=task_repo)

    def get_task_async_service_transactional(
        task_repo: TaskAsyncRepoTransactionDep,
    ) -> TaskAsyncService:
        return TaskAsyncService(task_repo=task_repo)

    TaskAsyncServiceDep = Annotated[TaskAsyncService, Depends(get_task_async_service_read_only)]
    TaskAsyncServiceTransactionDep = Annotated[
        TaskAsyncService, Depends(get_task_async_service_transactional)
    ]
"""

from typing import Annotated

from fastapi import Depends

from dependencies.repositories import (
    AccountRepoDep,
    AccountRepoTransactionDep,
    PostRepoDep,
    PostRepoTransactionDep,
)
from services.account_service import AccountService
from services.board_service import BoardService


# ── Account Service DI ──
def get_account_service_read_only(account_repo: AccountRepoDep) -> AccountService:
    return AccountService(account_repo=account_repo)


def get_account_service_transactional(
    account_repo: AccountRepoTransactionDep,
) -> AccountService:
    return AccountService(account_repo=account_repo)


AccountServiceDep = Annotated[AccountService, Depends(get_account_service_read_only)]
AccountServiceTransactionDep = Annotated[
    AccountService, Depends(get_account_service_transactional)
]


# ── Board Service DI (Post + Account 조합) ──
def get_board_service_read_only(
    post_repo: PostRepoDep, account_repo: AccountRepoDep
) -> BoardService:
    return BoardService(post_repo=post_repo, account_repo=account_repo)


def get_board_service_transactional(
    post_repo: PostRepoTransactionDep, account_repo: AccountRepoTransactionDep
) -> BoardService:
    return BoardService(post_repo=post_repo, account_repo=account_repo)


BoardServiceDep = Annotated[BoardService, Depends(get_board_service_read_only)]
BoardServiceTransactionDep = Annotated[
    BoardService, Depends(get_board_service_transactional)
]
