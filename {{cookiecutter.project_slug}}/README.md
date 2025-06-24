# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## 🚀 Quick Start

### Prerequisites
- Python {{cookiecutter.python_version}}+
- PostgreSQL (for production)

### Local Development

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd {{cookiecutter.project_slug}}
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to see your app!

## 🌐 Deployment to Render.com

### Automatic Deployment
1. **Connect to GitHub**: Link your Render account to this repository
2. **Create Web Service**: Render will automatically detect `render.yaml`
3. **Environment Variables**: Set in Render dashboard (SECRET_KEY is auto-generated)
4. **Deploy**: Push to main branch triggers automatic deployment

### Manual Deployment Steps
1. Fork/clone this repository
2. Connect to Render.com
3. Create a new Web Service
4. Connect your GitHub repository
5. Render will automatically:
   - Install dependencies
   - Run database migrations
   - Collect static files
   - Start the application

## 📁 Project Structure

```
{{cookiecutter.project_slug}}/
├── {{cookiecutter.project_slug}}/          # Django project settings
├── apps/
│   └── {{cookiecutter.app_name}}/          # Main application
│       ├── templates/                      # HTML templates
│       ├── views.py                        # View functions
│       └── urls.py                         # URL routing
├── static/                                 # Static files
├── templates/                              # Global templates
│   └── base.html                          # Base template with Tailwind CSS + HTMX
├── render.yaml                            # Render.com deployment config
├── requirements.txt                       # Python dependencies
└── .github/workflows/                     # CI/CD pipeline
```

## 🛠 Features

- ✅ **Django 5.2** - Latest Django version
- ✅ **PostgreSQL** - Production-ready database
- ✅ **Tailwind CSS** - Modern utility-first CSS framework
- ✅ **HTMX** - Dynamic interactions without JavaScript complexity
- ✅ **WhiteNoise** - Static file serving
- ✅ **Render.com Ready** - Zero-config deployment
- ✅ **CI/CD** - GitHub Actions integration
- ✅ **Resume Page** - Sample portfolio page at `/about/`

## 🎨 Frontend Stack

- **Tailwind CSS**: Utility-first CSS framework loaded via CDN
- **HTMX**: Enables dynamic interactions with minimal JavaScript
- **Responsive Design**: Mobile-first approach
- **Modern UI**: Clean, professional design

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Django secret key (auto-generated on Render)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: PostgreSQL connection string (auto-set by Render)

### Local Development
For local development, you can use SQLite (default) or PostgreSQL:

```python
# Using PostgreSQL locally
DATABASE_URL=postgres://username:password@localhost/database_name
```

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 📝 Customization

1. **Update Resume**: Edit `apps/{{cookiecutter.app_name}}/templates/{{cookiecutter.app_name}}/about.html`
2. **Add Models**: Create models in `apps/{{cookiecutter.app_name}}/models.py`
3. **Custom Styles**: Add CSS to `templates/base.html` or create separate CSS files
4. **New Views**: Add views to `apps/{{cookiecutter.app_name}}/views.py` and URLs to `urls.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

Built with ❤️ using Django, Tailwind CSS, and HTMX. Deployed on Render.com.