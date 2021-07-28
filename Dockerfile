FROM python:3.8

#RUN npm install -g nodemon

#FROM tiangolo/uvicorn-gunicorn-fastapi

#RUN pip install poetry

WORKDIR /app

ADD src/ src/
COPY docker-entrypoint.sh requirements.txt ./

#RUN poetry install
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# Install app related dependencies
#ENV POETRY_VIRTUALENVS_IN_PROJECT true

CMD ["bash", "docker-entrypoint.sh"]
