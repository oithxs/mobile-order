FROM python

ENV FLASK_APP app

ENV FLASK_ENV development

WORKDIR /usr/src/app

COPY ./requirements.txt ./

COPY ./ /usr/src/app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt