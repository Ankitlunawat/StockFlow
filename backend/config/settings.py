from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
import os
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','local-demo-only-do-not-deploy')
DEBUG=True
ALLOWED_HOSTS=['localhost','127.0.0.1','testserver']
INSTALLED_APPS=['django.contrib.contenttypes','django.contrib.auth','django.contrib.sessions','django.contrib.staticfiles','inventory']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware']
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
ROOT_URLCONF='config.urls'
STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR.parent/'frontend'/'dist']
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
