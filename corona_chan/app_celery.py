from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


__all__ = [ 'corona_chan_task' ]

os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'corona_chan.settings' )

corona_chan_task = Celery( 'corona_chan' )

corona_chan_task.config_from_object( 'django.conf:settings' )
corona_chan_task.autodiscover_tasks( lambda: settings.INSTALLED_APPS )
