FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN pip install python-decouple

COPY . /app

CMD [ "python", "Server.py" ]
