# Django Render.com Deployment Boilerplate PRD

## 개요
Render.com에 즉시 배포 가능한 Django 프로젝트 boilerplate를 cookiecutter를 통해 생성하는 도구

## 목표
- `django-admin startproject` 실행 시 주소 지정으로 한번에 생성
- cookiecutter 기반 템플릿 제공
- 생성 후 즉시 render.com 배포 가능

## 핵심 기능

### 1. Cookiecutter 템플릿 구성
- 프로젝트명, 앱명 등 기본 설정 커스터마이징
- PostgreSQL 데이터베이스 설정 포함 (Render 기본 지원)
- 환경변수 기반 설정 관리

### 2. Render.com 배포 준비
- `render.yaml` 배포 설정 파일
- `requirements.txt` 의존성 관리
- 정적 파일 및 미디어 파일 처리
- PostgreSQL 데이터베이스 연결 설정
- 자동 마이그레이션 수행

### 3. Django 프로젝트 기본 구성
- 프로덕션 환경 설정 (DEBUG=False)
- ALLOWED_HOSTS 설정
- 기본 앱 구조 및 모델
- `/about/` 경로에 이력서 샘플 페이지

### 4. 프런트엔드 구성
- Tailwind CSS CDN 통합
- HTMX 적용으로 동적 인터랙션 지원
- 반응형 디자인

### 5. CI/CD 파이프라인
- GitHub Actions 설정
- 자동 테스트 및 배포
- 코드 품질 검사

## 기술 스택
- Python 3.11+
- Django 5.2
- PostgreSQL (Render 관리형)
- Gunicorn (WSGI 서버)
- WhiteNoise (정적 파일)
- Tailwind CSS (CDN)
- HTMX
- Cookiecutter

## 프로젝트 구조
```
{{cookiecutter.project_name}}/
├── {{cookiecutter.project_name}}/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── resume/
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           └── resume/
│               └── about.html
├── static/
├── templates/
│   └── base.html
├── render.yaml
├── requirements.txt
├── manage.py
└── .github/
    └── workflows/
        └── deploy.yml

## 배포 후 확인 항목
1. 정적 파일 정상 로드 (Tailwind CSS)
2. 데이터베이스 마이그레이션 완료
3. 관리자 페이지 접근 가능
4. `/about/` 이력서 페이지 정상 표시
5. HTMX 동작 확인