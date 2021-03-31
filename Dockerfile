# pull official base image
FROM python:3.9

RUN apt-get update \
    && apt-get install -yyq netcat

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]