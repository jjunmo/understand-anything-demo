# Understand-Anything 데모

[Understand-Anything](https://github.com/Lum1104/Understand-Anything) 도구를 소개하는 **세미나용 데모 저장소**입니다.
코드베이스를 인터랙티브 지식 그래프로 변환하는 도구가 실제로 어떤 결과를 내는지 보여주기 위해 만들어졌습니다.

> **이 repo의 목적**: "도구를 도입하자"가 아니라 **"이런 기술이 있더라"는 지식 공유**.
> 실제 운영 코드(`aiapp-service`)를 외부 LLM에 보내지 않고, **동일한 아키텍처를 본뜬 데모 코드**에 도구를 돌려 체감을 전달합니다.

---

## 왜 이 코드인가

이 데모는 [jjunmo-fastapi-boilertemplate](https://github.com/jjunmo/jjunmo-fastapi-boilertemplate)을 기반으로,
실제 서비스(`aiapp-service`)와 **동일한 아키텍처 패턴**을 따르도록 두 도메인(`account`, `board`)을 추가한 FastAPI 앱입니다.

| 패턴 | 이 데모 | aiapp-service |
|------|---------|---------------|
| 계층 구조 | api → service → repository → model | router → service → repository → model |
| 제네릭 리포지토리 | `BaseRepository[T]` | `BaseRepository` |
| DI 방식 | 읽기/트랜잭션 분리 Type Alias | `ServiceDep` / `ServiceTransactionDep` |
| 스택 | FastAPI + SQLAlchemy 2.0 + Pydantic v2 + Alembic | 동일 |

→ 그래서 이 데모의 지식 그래프 구조가 곧 우리 실제 서비스의 구조와 닮아 있습니다.

## 무엇이 들어 있나

```
api/routes/account.py     회원가입 / 로그인 / 계정 조회
api/routes/board.py       게시글 작성 / 목록 / 단건 조회
services/account_service  회원 인증 비즈니스 로직 (ServiceException 활용)
services/board_service    게시글 CRUD (작성자 검증 → account 도메인 참조)
util/security.py          비밀번호 해싱 (데모용)
models/account.py         Account 엔티티
models/board.py           Board, Post 엔티티 (Post.author_id → Account)
```

- **두 도메인 클러스터** (account / board) + **도메인 간 관계** (`Post.author_id → Account`)
- 그래프에서 인증 흐름, 게시판 흐름, 둘 사이의 의존이 시각적으로 드러나도록 구성

---

## 도구 실행 방법 (데모 재현)

Understand-Anything은 **Claude Code 플러그인**입니다. 이 repo를 분석 대상으로 아래를 실행합니다.

```bash
# 0. 이 repo 클론
git clone https://github.com/jjunmo/understand-anything-demo.git
cd understand-anything-demo
```

Claude Code 안에서 (슬래시 명령):

```bash
# 1. 플러그인 설치
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything

# 2. 코드베이스 분석 → .understand-anything/knowledge-graph.json 생성
/understand --language ko

# 3. 인터랙티브 대시보드 보기
/understand-dashboard
```

### 데모 장면별 명령

| 장면 | 명령 | 보여주는 것 |
|------|------|------------|
| 전체 지도 | `/understand-dashboard` | 계층·도메인 클러스터 전체 |
| 의미 검색 | `/understand-chat 로그인 인증은 어디서 처리하나?` | account 클러스터 하이라이트 |
| 가이드 투어 | `/understand-onboard` | 의존성 순서 학습 경로 |
| 파일 설명 | `/understand-explain services/account_service.py` | 특정 파일 심층 설명 |
| 도메인 매핑 | `/understand-domain` | 코드↔비즈니스 대응 |

> 지원 언어: en(기본), zh, zh-TW, ja, **ko**, ru

---

## 앱 자체 실행 (선택)

도구 분석은 정적 파싱이라 앱 실행이 필수는 아니지만, 직접 돌려보려면:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
# http://localhost:8000/docs 에서 Swagger 확인
```

테스트:

```bash
pytest tests/ -v
```

---

## 관련

- 도구 원본: https://github.com/Lum1104/Understand-Anything
- 기반 보일러템플릿: https://github.com/jjunmo/jjunmo-fastapi-boilertemplate
- 라이브 데모(공식): https://understand-anything.com
