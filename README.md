# SeedyFiuba Notifications Microservice

This is a microservice that provides push notifications functionalities to SeedyFiuba backend.

### Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Docker](https://www.docker.com/)

### Deployed In

* [Heroku](https://www.heroku.com/) as a Container Registry.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Docker-cli must be installed.

### Installation

1. Clone the repo
   ```git
   git clone https://github.com/Taller2SeedyFiuba/Seedyfiuba_Back_Notifications
   ```
2. [Install Docker](https://docs.docker.com/engine/install/), following it's official installation guide for your os 

3. Set up environment variables in an ```.env``` named file based on ```.env.example```.

## Usage

```docker
docker-compose up --build
```

### Docs

Swagger is used to document the API structure, FastAPI provide us automatic swagger documentation
```
{HOST}/api/docs
{HOST}/api/redoc
```

### Standars

* [Jsend](https://github.com/omniti-labs/jsend) standars were followed up on the API design


## Production Deployment CI

This repository is configured using GitHub Actions. When ```main``` is updated an automated deploy is done using CI.

### GitHub Actions secrets

* HEROKU_API_KEY
* HEROKU_APP_NAME

## License
[MIT](https://choosealicense.com/licenses/mit/)
