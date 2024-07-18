# initialize_DRF

## 소개

이 프로젝트는 Django와 Django REST Framework (DRF)를 독창적이고 개인화된 설정으로 구성하는 것을 목표로 합니다.

<br>

## 진행 방식
- 각 설정 변경 사항마다 커밋
- 주간 회의:
    - 시간: 저녁 9시 ~ 10시 30분
    - 형식: 초기 전체 회의 → 짝 매칭 후 리뷰 및 토론 → 각자 발표 → 최종 그룹 회의로 의견 나눔

<br>

## 목표
- 기본적인 설정은 공식 문서나 블로그에 많지만, 자신만의 독특한 Django 설정을 구현
- 설정값들을 무작정 사용하는 것이 아니라, 장단점을 비교해보고 자신만의 것으로 만듬
- 나만의 설정을 제대로 해놓음으로써 이후 프로젝트에서 포크를 사용하여 편리하게 진행할 수 있도록 구현

<br>

## 구현 기능
### AUTH
- JWT를 이용하여 인증 및 권한 관리

### BOARD
- 기본적인 CRUD 구현

### 환경 변수 관리
- 보안적인 요소를 고려하여 환경 변수를 효율적으로 관리
- 민감한 정보(예: 데이터베이스 비밀번호, API 키, 시크릿 키 등)를 소스 코드에 직접 포함시키지 않고, 환경 변수 파일을 사용하여 관리
- Django-environ 사용

### LOGGING
- 개발환경: 콘솔에 DEBUG 레벨 출력, ERROR이상은 errors.log에 기록
- 배포환경: 파일에 DEBUG 레벨 출력, ERROR이상은 errors.log에 기록

### CUSTOM PAGINATION
- 커스텀 페이지네이션 기능 구현

### CUSTOM EXCEPTION
- 프로젝트의 특성과 요구사항에 맞게 커스텀 예외 처리를 구현
- 특정한 상황에서 발생할 수 있는 예외들을 정의하고, 이를 효과적으로 핸들링하여 사용자에게 적절한 에러 메시지를 제공하는 기능을 구현
- 예외 발생 시 로깅 및 알림 기능을 추가하여 문제 해결을 용이하게 함

### CUSTOM RESPONSE
- 클라이언트가 일관된 방식으로 데이터를 처리할 수 있도록 응답 데이터의 형식을 통일하고, 필요한 경우 추가 정보를 포함한 응답을 제공하기 위해 커스텀 응답 처리를 구현

### CUSTOM RENDER
- 데이터의 렌더링 방식을 커스터마이징하여 클라이언트에게 최적화된 포맷으로 데이터를 제공
- RESPONSE를 사용중이므로 현재 비활성화 상태

### CUSTOM JWT TOKEN
- 기본적인 JWT 토큰 외에, 프로젝트 요구사항에 맞는 커스텀 JWT 토큰 기능을 구현
- 토큰의 유효 기간, 클레임, 시크릿 키 등을 설정하고, 토큰 갱신 기능
-   토큰 검증 절차를 강화하여 보안성을 높이고, 토큰과 관련된 각종 예외 상황을 처리합니다.

### SWAGGER 
- API 문서화를 위해 drf-yasg를 사용하여 Swagger 설정을 구성
- API 엔드포인트를 시각화하고, 인터랙티브 문서를 제공

### GITHUB
- Pre-commit 설정
- Issues 관리
- PR (Pull Request) 관리
- Labels 설정

<br>

## 설치 및 설정


### 필수 조건
- Python 3.11
- Django 5.0.4
- Django REST Framework 3.15.1

### 설치 방법
1. 저장소를 클론합니다.
   ```bash
   git clone <저장소 URL>
   cd <프로젝트 디렉토리>

2. 가상환경 만들기
   ```bash
    python -m venv venv

3. 가상환경을 활성화 시켜줍니다.
- Windows
    ```bash
    venv\Scripts\activate

- MacOS/Linux
    ```bash
    source venv/bin/activate

4. requirements.txt에 있는 의존성 파일 설치
   ```bash
    pip install -r requirements.txt

4. .env 파일 설정

5. Django의 데이터 베이스를 마이그레이션 & 마이그레이트
   ```bash
    make makemigrations
    make migrate

6. 실행
   ```bash
    make run
