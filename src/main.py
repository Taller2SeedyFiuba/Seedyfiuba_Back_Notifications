from src.utils.log import logInfo
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from .api.routes import index
from .api.errors.ApiError import ApiError
from .api.errors.handlers import *
from .database.start import startDatabase
from fastapi.middleware.cors import CORSMiddleware

startDatabase()

logInfo('Starting Application')
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ApiError, ApiErrorHandler)
app.add_exception_handler(RequestValidationError, RequestValidationErrorHandler)
app.add_exception_handler(HTTPException, HTTPExceptionHandler)
app.add_exception_handler(Exception, ExceptionHandler)
app.include_router(index.router, prefix='/api')
