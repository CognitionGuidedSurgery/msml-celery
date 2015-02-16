#!/bin/bash

export CELERY_CONFIG_MODULE="celeryconfig"
celery -A msmlcelery worker --loglevel=info
