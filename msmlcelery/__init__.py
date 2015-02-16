__author__ = 'Alexander Weigl'

from celery import Celery

app = Celery("msmlcelery")
app.config_from_envvar("CELERY_CONFIG_MODULE")
#"celeryconfig")


import sys
sys.path.append("../msml/src")
import msml.frontend, msml.sorts
import tempfile
msml_alphabet = msml.frontend.App().alphabet

def create_temp_file(content, suffix):
    fd,name = tempfile.mkstemp(suffix)
    with open(name, 'w') as fd:
        fd.write(content)
    return name

def read_content(filename):
    with open(filename, 'r') as fd:
        return fd.read()

def wrap(operator):
    """`wrap` decorates a operator for return the file contents instead of the filename.
    :param operator: an operator to be wrapped
    """

    def fn(**kwargs):
        for i in operator.input.values():
            if issubclass(i.sort.physical, msml.sorts.InFile):
                kwargs[i.name] = create_temp_file(kwargs[i.name], suffix=i.sort.physical.__name__.lower())

        for p in operator.parameters.values():
            if p.target:
                kwargs[p.name] = create_temp_file(kwargs[p.name],
                                                  suffix=p.sort.physical.__name__.lower())

        print kwargs

        result = operator(**kwargs)

        for k in result:
            slot = operator.output[k]
            if issubclass(slot.sort.physical, msml.sorts.InFile):
                result[k] = read_content(result[k])

        return result

    return fn

ns = globals()
for operator in msml_alphabet.operators.values():
    ns[operator.name] = app.task(name = operator.name)(wrap(operator))

