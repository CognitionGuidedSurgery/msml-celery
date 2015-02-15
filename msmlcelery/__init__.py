__author__ = 'Alexander Weigl'

from celery import Celery

app = Celery("msmlcelery")
celery.config_from_envvar("CELERY_CONFIG_MODULE")


import sys
sys.path.append("../msml/src")
import msml.frontend
msml_alphabet = msml.frontend.App().alphabet

for operator in msml_alphabet.operators.values():
    __dict__[operator.name] = app.task(name = operator.name)(operator)

