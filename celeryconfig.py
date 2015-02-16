__author__ = 'Alexander Weigl'

import os

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://guest:guest@i61sv002:5672//')
#CELERY_RESULT_BACKEND = 'redis://i61sv002/0'
CELERY_RESULT_BACKEND = 'amqp'
CELERY_IMPORTS = ('msmlcelery', )

# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Europe/Berlin'
CELERY_ENABLE_UTC = True