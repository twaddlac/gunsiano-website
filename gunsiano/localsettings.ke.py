DEBUG = True

SECRET_KEY = 'p9^@trv$zy0fo=o@r%o+%#(9_whberi1zi=q8fpmb)rao=zqvb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'dev',
        'PASSWORD': '5PkGwukACP',
        'NAME': 'gunsiano',
    }
}

STATIC_ROOT = 'staticfiles'

MEDIA_ROOT = 'mediafiles'

# Turn off in dev
# GOOGLE_ANALYTICS_ID = 'UA-10086645-4'
GOOGLE_ANALYTICS_ID = ''
