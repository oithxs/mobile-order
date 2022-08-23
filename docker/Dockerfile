FROM python

WORKDIR /usr/src/app

COPY ./requirements.txt ./

COPY ./app /usr/src/app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt