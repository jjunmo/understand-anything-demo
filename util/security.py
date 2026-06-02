"""
비밀번호 해싱 유틸 (데모용)
==========================
실제 운영에서는 bcrypt/argon2 등을 사용해야 한다.
본 템플릿은 도구 분석/데모 목적이므로 표준 라이브러리 hashlib로 단순 구현한다.
"""

import hashlib
import secrets


def hash_password(plain_password: str) -> str:
    """평문 비밀번호를 salt와 함께 해싱한다."""
    salt = secrets.token_hex(16)
    digest = hashlib.sha256((salt + plain_password).encode()).hexdigest()
    return f"{salt}${digest}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """평문 비밀번호가 저장된 해시와 일치하는지 검증한다."""
    try:
        salt, digest = hashed_password.split("$", 1)
    except ValueError:
        return False
    expected = hashlib.sha256((salt + plain_password).encode()).hexdigest()
    return secrets.compare_digest(expected, digest)
