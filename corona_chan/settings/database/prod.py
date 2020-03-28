import os


#mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ[ 'CORONA_CHAN__DATABASE__NAME' ],
        'USER': os.environ[ 'CORONA_CHAN__DATABASE__USER' ],
        'PASSWORD': os.environ[ 'CORONA_CHAN__DATABASE__PASSWORD' ],
        'HOST': os.environ[ 'CORONA_CHAN__DATABASE__HOST' ],
        'PORT': os.environ[ 'CORONA_CHAN__DATABASE__PORT' ],
    },
}
