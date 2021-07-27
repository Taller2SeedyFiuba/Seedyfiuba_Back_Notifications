#!/bin/bash

poetry run uvicorn "src.main:app" --port $PORT --reload #--host ${HOST}

