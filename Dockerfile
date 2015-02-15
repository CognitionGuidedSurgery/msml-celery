FROM wadoon/msml

MAINTAINER Alexander Weigl <Alexander.Weigl@student.kit.edu>

ENV PYTHONPATH /app

ADD . /app

WORKDIR /app

RUN sudo pip install -r requirements.txt

CMD /app/worker.sh