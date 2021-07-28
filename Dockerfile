#FROM nikolaik/python-nodejs:latest

#RUN npm install -g nodemon

FROM tiangolo/uvicorn-gunicorn-fastapi

#RUN pip install poetry

WORKDIR /app

ADD src/ src/
COPY docker-entrypoint.sh poetry.lock pyproject.toml requirements.txt ./

#RUN poetry install

RUN pip install -r ./requirements.txt

# Install app related dependencies
ENV POETRY_VIRTUALENVS_IN_PROJECT true

CMD ["bash", "docker-entrypoint.sh"]
