FROM tiangolo/uvicorn-gunicorn-fastapi

# Install Heroku GPG dependencies
RUN apt-get install -y gpg apt-transport-https gpg-agent curl ca-certificates


# Datadog ENVs

ENV DD_APM_ENABLED=true
ENV DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true
ENV DD_DYNO_HOST=false
ENV DATADOG_APT_KEYRING="/usr/share/keyrings/datadog-archive-keyring.gpg"
ENV DATADOG_APT_KEYS_URL="https://keys.datadoghq.com"


# Add Datadog repository and signing keys
RUN sh -c "echo 'deb [signed-by=${DATADOG_APT_KEYRING}] https://apt.datadoghq.com/ stable 7' > /etc/apt/sources.list.d/datadog.list"
RUN touch ${DATADOG_APT_KEYRING}
RUN curl -o /tmp/DATADOG_APT_KEY_CURRENT.public "${DATADOG_APT_KEYS_URL}/DATADOG_APT_KEY_CURRENT.public" && \
    gpg --ignore-time-conflict --no-default-keyring --keyring ${DATADOG_APT_KEYRING} --import /tmp/DATADOG_APT_KEY_CURRENT.public
RUN curl -o /tmp/DATADOG_APT_KEY_F14F620E.public "${DATADOG_APT_KEYS_URL}/DATADOG_APT_KEY_F14F620E.public" && \
    gpg --ignore-time-conflict --no-default-keyring --keyring ${DATADOG_APT_KEYRING} --import /tmp/DATADOG_APT_KEY_F14F620E.public
RUN curl -o /tmp/DATADOG_APT_KEY_382E94DE.public "${DATADOG_APT_KEYS_URL}/DATADOG_APT_KEY_382E94DE.public" && \
    gpg --ignore-time-conflict --no-default-keyring --keyring ${DATADOG_APT_KEYRING} --import /tmp/DATADOG_APT_KEY_382E94DE.public

# Install the Datadog agent
RUN apt-get update && apt-get -y --force-yes install --reinstall datadog-agent

# Set a working directory inside container
WORKDIR /app

# Copy entry point and application dependencies inside container
COPY heroku/heroku-entrypoint.sh ./

ADD src/ src/
COPY poetry.lock pyproject.toml requirements.txt ./

RUN pip install -r ./requirements.txt

# Expose DogStatsD and trace-agent ports
EXPOSE 8125/udp 8126/tcp

# Copy Datadog configuration
COPY heroku/datadog-config/ /etc/datadog-agent/

# Run entry point
CMD ["bash", "heroku-entrypoint.sh"]
