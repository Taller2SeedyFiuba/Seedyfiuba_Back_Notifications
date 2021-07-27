#!/bin/bash

poetry run uvicorn "src.main:app" --host ${HOST} --port $PORT --reload

