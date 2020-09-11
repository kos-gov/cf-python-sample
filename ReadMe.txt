1. Local PC에서 Testing 방법

	1) python manage.py runserver
	2) http://localhost:8000 or http://127.0.0.1

2. Cloud Foundry에서 Testing 방법

	1) static file들을 참조하지 못하는 문제가 있어서 반드시 아래 URL을 참조하여
	   필요한 조치를 취해야 한다.

	https://www.ianhuston.net/2017/10/bringing-django-to-cloud-foundry/
	(Bringing a Python Django app to Cloud Foundry in 2017)

	(1) manifest.yml 수정하기

		command: python manage.py collectstatic --noinput && gunicorn superlists.wsgi:application

	(2) requirements.txt 추가하기

		whitenoise=5.2.0

	(2) settings.py 수정하기

		MIDDLEWARE_CLASSES = [
		  'django.middleware.security.SecurityMiddleware',
		  'whitenoise.middleware.WhiteNoiseMiddleware',
		  # ...
		]

		TEMPLATES = [
		    {
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [os.path.join(BASE_DIR, 'templates')],
			'APP_DIRS': True,
			'OPTIONS': {
			    'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
			    ],
			},
		    },
		]

		# Static files (CSS, JavaScript, Images)
		# https://docs.djangoproject.com/en/3.0/howto/static-files/

		STATIC_URL = '/static/'
		STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
		STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

		STATICFILES_FINDERS = (
		    'django.contrib.staticfiles.finders.FileSystemFinder',
		    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
		)


