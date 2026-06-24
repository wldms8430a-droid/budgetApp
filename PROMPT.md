# Step 1. 프로젝트 뼈대 만들기

## 참고
```
초급 수준의 프로젝트로, 브랜치 정책, AI에게 Phase 별로 개발하도록 하는 방식 등은 포함하지 않음
```

### 1-1. AGENTS.md 먼저 생성
AGENTS.md는 Codex에게 프로젝트 규칙을 알려주는 설정 파일입니다.
이 파일이 있으면 매 프롬프트마다 규칙을 반복하지 않아도 됩니다.

[프롬프트 1 - AGENTS.md 생성 요청]
```
이 저장소는 Python CLI 가계부 앱 프로젝트야. 이 프로젝트를 위한 AGENTS.md, 서브에이전트, 관련 스킬을 먼저 만들어줘.
AGENTS.md 파일에 포함할 내용:
- 프로젝트 설명 (CSV 기반 가계부 CLI 앱)
- 코딩 규칙: 타입 힌트 필수, 함수 하나 최대 50줄
- TDD 규칙: 구현 전 반드시 테스트 먼저
- 품질 규칙: 순환복잡도 10 이하 유지
- 품질 검수 규칙: 커밋 전 반드시 qa_engineer 서브에이전트로 품질 검수
- 테스트 실행 명령어: pytest, radon cc
- 커밋 규칙: 하나의 기능이 개발되면 커밋, 푸시 진행
```

### 1-2. 프로젝트 구조 생성
[프롬프트 2 - 계획 요청]
```
가계부 CLI 앱의 전체 계획을 먼저 알려줘.
- 어떤 파일들이 필요한지
- 각 파일의 역할
- 구현 순서
코드는 아직 작성하지 마. 계획만 설명해줘.
```

[프롬프트 3 - 뼈대 파일 생성]
일반적으로 아래 구조는 우리가 제시할 필요가 없으나, 모두가 유사하게 진행하기 위해서 지정함
```
계획대로 프로젝트 뼈대를 만들어줘. 필요한 패키지는 설치해줘.
- budget/__init__.py 생성
- budget/core.py 생성 (함수 시그니처와 docstring만, 구현은 pass로)
- tests/__init__.py 생성
- tests/test_core.py 생성 (첫 번째 테스트만: test_add_transaction_increases_length)
- requirements.txt 생성 (pytest, pytest-cov, radon, xenon, flake8)
구현 코드는 아직 작성하지 마.
```

### 1-3. add_transaction TDD 구현
[프롬프트 4 - 테스트 확장]
```
tests/test_core.py에 add_transaction 테스트를 추가해줘.
data/step1_transactions.csv 파일을 참고해서
실제 데이터 형태에 맞는 테스트 케이스를 작성해줘.
테스트 케이스:
1. 거래 추가 후 목록 길이 증가 확인
2. 음수 amount (지출) 정상 저장 확인
3. 양수 amount (수입) 정상 저장 확인
4. 빈 description 처리 확인
아직 구현은 하지 마.
```

[프롬프트 5 - 구현]
```
이제 budget/core.py의 add_transaction 함수를 구현해줘.
- 방금 작성한 테스트를 모두 통과해야 해
- 순환복잡도 5 이하
- 타입 힌트 필수
- 거래 데이터는 딕셔너리로 저장: date, type, category, description, amount, memo 필드
```

# Step 2: get_balance + filter_by_category

### 2-1: get_balance 
[프롬프트 6 - 계획]
```
get_balance 함수를 추가하려 해. 구현 전에 계획을 먼저 말해줘.
data/step2_transactions.csv를 열어서 데이터 구조를 파악하고,
어떤 테스트 케이스가 필요한지 설명해줘.
```

[프롬프트 7 - 테스트 + 구현]
```
get_balance 함수의 테스트를 tests/test_core.py에 추가하고,
budget/core.py에 구현도 해줘.
- 수입(양수)과 지출(음수)의 합계를 반환
- 빈 리스트면 0.0 반환
- step2_transactions.csv 데이터로 검증 가능한 테스트 포함
```

### 2-2: filter_by_category
[프롬프트 8]
```
filter_by_category 함수를 추가해줘.
data/step2_transactions.csv의 실제 카테고리명을 사용해서 테스트 작성.
- 카테고리 대소문자 구분 없이 매칭
- 없는 카테고리면 빈 리스트 반환
- 결과가 원본 리스트와 독립적인지 확인하는 테스트 포함
```

# Step 3. 개선사항 확인
추가가 필요한 요구사항 확인

# Step 4: monthly_summary
### 4-1. CSV 파일 로드 기능 추가 

[프롬프트 9]
```
budget/core.py에 CSV 파일을 읽어서 거래 목록을 반환하는
load_transactions_from_csv 함수를 추가해줘.
- data/step3_transactions.csv 형태의 파일을 읽어야 해
- 인코딩은 utf-8-sig (BOM 포함 CSV 호환)
- amount 필드는 int로 변환
- 테스트도 함께 작성해줘 (step1_transactions.csv로 검증)
```

### 4-2. monthly_summary 구현
[프롬프트 10 - 의도적으로 복잡하게]
```
monthly_summary 함수를 추가해줘.
- 거래 목록에서 월별(YYYY-MM) 수입 합계, 지출 합계, 순이익을 계산
- 반환: {"2026-01": {"income": 3500000, "expense": -158300, "net": 3341700}, ...}
- 일단 동작하는 코드로 먼저 작성해줘 (최적화는 다음 단계에서)
```

### 4-3. 리팩토링 (서브에이전트 활용)
[프롬프트 11]
```
QA 서브에이전트를 활용해서 품질 관점에서 다음을 검사하고 개선 방안을 제시해줘
1. 모든 함수에 타입 힌트가 있는가?
2. 순환복잡도 10 초과 함수가 있는가?
3. 엣지 케이스가 테스트되지 않은 함수가 있는가?
4. data/step4_large_transactions.csv (5000건) 로드 시 문제가 생길 코드가 있는가?
```

# Step 5: GitHub Actions CI 설정
학습 목표: Codex가 CI 설정 파일을 생성하고, Push 시 자동 품질 검사 확인

### 5-1. CI 파일 생성
[프롬프트 12]
```
이 프로젝트에 GitHub Actions CI를 추가해줘.
포함할 검사:
1. pytest 실행 (실패 시 빌드 중단)
2. 테스트 커버리지 100% 이하면 실패
3. radon/xenon으로 순환복잡도 B등급 초과 시 실패
4. flake8 스타일 검사
트리거: main 브랜치 push 및 PR
```

# Step 6: 대용량 데이터 테스트 (10분)
[프롬프트 15]
```
tests/test_core.py에 대용량 데이터 테스트를 추가해줘.
data/step4_large_transactions.csv (5000건)를 사용해서:
1. 5000건 로드 후 load_transactions_from_csv가 정상 동작하는지
2. get_balance가 올바른 값을 반환하는지
3. monthly_summary가 65개 이상의 월 데이터를 처리하는지 (2020~2026년)
```


# 매우 쉽게 진행하고 싶은 경우
```
csv 비용 파일을 읽어서 웹으로 표현하는 가계부 프로그램을 만들고 싶어.
data 폴더에 샘플 파일이 있으니까 프로젝트 구조 생성하고 작업 계획 제시해.
다음은 반드시 지켜줘
- 소스코드는 TDD 방식으로 개발해
- 소스코드 커버리지는 브랜치 커버리지 100%를 반드시 달성해
- 소스코드 정적분석 해줘.
- 함수 순환복잡도는 10 이하 유지
- Github Action에서 검사
- 브랜치 정책 유지
- QA 서브에이전트와 적절한 스킬을 적용해서, 매 Phase마다 검사
- Python으로 개발

다음 기능은 반드시 포함해줘
- 일, 월간 단위 통계 표시
- csv 파일 업로드 기능
- 대용량 파일에 대한 처리
```
