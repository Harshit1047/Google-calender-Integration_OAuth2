import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '640eb7ab-0b74-4154-9bbb-ef8c5c86ec77.id.repl.co',
    # Add any other allowed hosts here
]


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'urls'

GOOGLE_CLIENT_SECRET_FILE = '/client_secret_1078779531765-iafatrdufnrjtsc8d2d6it4ddfq5vv8n.apps.googleusercontent.com.json'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
