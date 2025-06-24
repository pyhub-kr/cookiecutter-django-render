# Django Render.com Cookiecutter Template

Django 프로젝트를 빠르게 생성하고 Render.com에 배포할 수 있는 cookiecutter 템플릿입니다.

## 요구사항

- Python 3.8+
- cookiecutter

## 설치

```bash
pip install cookiecutter
```

## 사용법

### 1. 프로젝트 생성

```bash
cookiecutter https://github.com/pyhub-kr/cookiecutter-django-render
```

또는 로컬 템플릿 사용:

```bash
cookiecutter /path/to/cookiecutter-django-render
```

### 2. 설정 옵션

프로젝트 생성 시 다음 옵션들을 설정할 수 있습니다:

- `project_name`: 프로젝트 이름 (기본값: "Django Render Project")
- `project_slug`: 프로젝트 폴더명 (자동 생성)
- `description`: 프로젝트 설명
- `author_name`: 작성자 이름
- `author_email`: 작성자 이메일
- `version`: 프로젝트 버전 (기본값: "0.1.0")
- `django_version`: Django 버전 (기본값: "5.2")
- `python_version`: Python 버전 (기본값: "3.11")
- `app_name`: Django 앱 이름 (기본값: "resume")
- `use_https`: HTTPS 사용 여부 (기본값: "y")

### 3. 생성되는 프로젝트 구조

```
your_project/
├── README.md
├── requirements.txt
├── render.yaml                 # Render.com 배포 설정
├── manage.py
├── your_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── your_app/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│       └── templates/
├── templates/
│   └── base.html
└── static/
```

### 4. 로컬 개발 환경 설정

생성된 프로젝트 디렉토리로 이동:

```bash
cd your_project_name
```

가상환경 생성 및 활성화:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

의존성 설치:

```bash
pip install -r requirements.txt
```

데이터베이스 마이그레이션:

```bash
python manage.py makemigrations
python manage.py migrate
```

개발 서버 실행:

```bash
python manage.py runserver
```

### 5. Render.com 배포

1. GitHub에 프로젝트 업로드
2. Render.com 계정 생성 및 로그인
3. "New Web Service" 선택
4. GitHub 저장소 연결
5. 배포 설정:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn your_project.wsgi:application`
   - **Environment**: `Python 3`

환경 변수 설정:
- `PYTHON_VERSION`: `3.11`
- `DATABASE_URL`: (PostgreSQL 데이터베이스 URL)
- `SECRET_KEY`: (Django 시크릿 키)
- `DEBUG`: `False`

### 6. 기본 제공 기능

- **반응형 디자인**: Tailwind CSS 사용
- **HTMX 통합**: 동적 웹 인터페이스
- **PostgreSQL 지원**: 프로덕션 환경용
- **정적 파일 관리**: WhiteNoise 사용
- **보안 설정**: 프로덕션 환경 최적화

## 개발 가이드

### 새로운 앱 추가

```bash
python manage.py startapp new_app
```

`settings.py`의 `INSTALLED_APPS`에 추가:

```python
INSTALLED_APPS = [
    # ...
    'apps.new_app',
]
```

### 정적 파일 관리

정적 파일은 `static/` 디렉토리에 저장하고, 프로덕션 배포 시 자동으로 수집됩니다.

### 템플릿 사용

기본 템플릿은 `templates/base.html`을 확장하여 사용:

```html
{% extends 'base.html' %}

{% block content %}
<h1>My Page</h1>
{% endblock %}
```

## 문제 해결

### 일반적인 문제들

1. **Static 파일이 로드되지 않음**
   - `python manage.py collectstatic` 실행
   - `STATIC_URL` 설정 확인

2. **데이터베이스 연결 오류**
   - `DATABASE_URL` 환경 변수 확인
   - PostgreSQL 서비스 상태 확인

3. **배포 실패**
   - `requirements.txt` 파일 확인
   - 환경 변수 설정 확인

## 라이센스

MIT License

## 기여

이슈 리포트나 풀 리퀘스트를 환영합니다!