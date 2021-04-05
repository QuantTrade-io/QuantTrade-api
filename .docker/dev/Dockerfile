# pull official base image
FROM python:3.9

RUN apt-get update \
    && apt-get install -yyq netcat

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy any files over
# COPY ../.docker/dev/entrypoint.sh .

# Change permissions
# RUN chmod +x /entrypoint.sh


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]