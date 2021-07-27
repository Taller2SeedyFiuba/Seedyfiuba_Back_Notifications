#FROM nikolaik/python-nodejs:latest

#RUN npm install -g nodemon

FROM python:3.8

RUN pip install poetry

WORKDIR /app

ADD src/ src/
COPY docker-entrypoint.sh poetry.lock pyproject.toml ./

RUN poetry install

# Install app related dependencies
ENV POETRY_VIRTUALENVS_IN_PROJECT true

CMD ["bash", "docker-entrypoint.sh"]
