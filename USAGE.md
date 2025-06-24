# Cookiecutter Django Render Template 사용 가이드

## 🚀 빠른 시작

### 1. cookiecutter 설치
```bash
pip install cookiecutter
```

### 2. 프로젝트 생성
```bash
cookiecutter https://github.com/yourusername/cookiecutter-django-render
```

### 3. 프로젝트 설정
```bash
# 생성된 프로젝트 디렉토리로 이동
cd your-project-name

# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env
# .env 파일을 편집하여 필요한 설정 입력

# 데이터베이스 마이그레이션
python manage.py migrate

# 관리자 계정 생성
python manage.py createsuperuser

# 개발 서버 실행
python manage.py runserver
```

## 📦 주소 지정으로 바로 생성하기

cookiecutter는 다음과 같이 직접 GitHub 주소를 지정하여 사용할 수 있습니다:

```bash
# HTTPS
cookiecutter https://github.com/yourusername/cookiecutter-django-render

# SSH
cookiecutter git+ssh://git@github.com/yourusername/cookiecutter-django-render

# 특정 브랜치 지정
cookiecutter https://github.com/yourusername/cookiecutter-django-render --checkout develop
```

## 🌐 Render.com 배포

### 방법 1: 자동 배포 (권장)
1. GitHub에 프로젝트 푸시
2. Render.com 계정으로 로그인
3. "New Web Service" 클릭
4. GitHub 리포지토리 연결
5. Render가 자동으로 `render.yaml` 감지하여 배포

### 방법 2: 수동 설정
1. Render.com에서 새 Web Service 생성
2. 다음 설정 입력:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn your_project.wsgi:application`
   - **Environment**: Python 3.11
3. 환경변수 설정:
   - `SECRET_KEY`: 자동 생성 또는 직접 입력
   - `DEBUG`: `false`
   - `ALLOWED_HOSTS`: `*` 또는 도메인 지정
4. PostgreSQL 데이터베이스 추가 (무료 플랜 사용 가능)

## 📋 사용자 정의

### 이력서 페이지 수정
`apps/resume/templates/resume/about.html` 파일을 편집:

```html
<!-- 이름과 이메일 변경 -->
<h1 class="text-4xl font-bold mb-2">{{ author_name }}</h1>
<p class="text-blue-200 mt-2">
    <a href="mailto:{{ author_email }}">{{ author_email }}</a>
</p>

<!-- 기술 스택 수정 -->
<span class="inline-block bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">
    Your Skill
</span>
```

### 새로운 앱 추가
```bash
# 새 앱 생성
python manage.py startapp your_new_app apps/your_new_app

# settings.py에 앱 추가
INSTALLED_APPS = [
    # ...
    'apps.your_new_app',
]
```

### 커스텀 모델 추가
`apps/resume/models.py`:
```python
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

마이그레이션 생성 및 적용:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🎨 스타일 커스터마이징

### Tailwind CSS 클래스 사용
```html
<!-- 기존 클래스 -->
<div class="bg-white rounded-lg shadow-sm p-8 fade-in">

<!-- 커스텀 스타일 추가 -->
<div class="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-8">
```

### HTMX 인터랙션 추가
```html
<!-- 동적 콘텐츠 로드 -->
<button hx-get="/api/data" hx-target="#content" 
        class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded">
    Load Data
</button>
<div id="content"></div>
```

## 🧪 테스트

### 기본 테스트 실행
```bash
python manage.py test
```

### 커버리지 확인
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # HTML 리포트 생성
```

## 🔧 개발 팁

### 1. 로컬 PostgreSQL 사용
```bash
# PostgreSQL 설치 (Ubuntu/Debian)
sudo apt-get install postgresql postgresql-contrib

# macOS (Homebrew)
brew install postgresql

# .env 파일에 DATABASE_URL 설정
DATABASE_URL=postgres://username:password@localhost/dbname
```

### 2. 정적 파일 관리
```bash
# 정적 파일 수집
python manage.py collectstatic

# 개발 중 정적 파일 서빙
python manage.py runserver --insecure
```

### 3. 디버그 모드
개발 중에는 `.env` 파일에서:
```
DEBUG=True
```

프로덕션에서는 반드시:
```
DEBUG=False
```

## 🔍 문제 해결

### 일반적인 오류들

1. **SECRET_KEY 오류**
   ```bash
   # 새 SECRET_KEY 생성
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **데이터베이스 연결 오류**
   - `DATABASE_URL` 환경변수 확인
   - PostgreSQL 서버 상태 확인

3. **정적 파일 로드 안됨**
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **HTMX 작동 안함**
   - CDN 로드 확인
   - 브라우저 개발자 도구에서 JavaScript 오류 확인

## 📞 지원

문제가 발생하면 다음을 확인해보세요:

1. **로그 확인**: Render.com 대시보드에서 배포 로그 확인
2. **환경변수**: 모든 필수 환경변수가 설정되었는지 확인
3. **의존성**: `requirements.txt`의 버전 호환성 확인
4. **GitHub Issues**: 프로젝트 저장소의 Issues 탭에서 비슷한 문제 검색

## 📈 다음 단계

1. **도메인 연결**: Render.com에서 커스텀 도메인 설정
2. **성능 최적화**: 캐싱, 압축 등 추가
3. **모니터링**: Sentry, 로그 관리 도구 연동
4. **백업**: 정기적인 데이터베이스 백업 설정

---

이 가이드로 Django 프로젝트를 Render.com에 성공적으로 배포하고 운영할 수 있습니다! 🎉