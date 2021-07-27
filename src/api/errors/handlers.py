from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from src.api.errors.ApiError import ApiError



def returnError(code : int, message : str) -> JSONResponse:
    return JSONResponse(
        status_code=code,
        content = {
            "status": "error",
            "message": message
            }
    )

def ApiErrorHandler(_: Request, exc: ApiError) -> JSONResponse:
    return returnError(exc.code, exc.message)

def RequestValidationErrorHandler(_: Request, exc: RequestValidationError) -> JSONResponse:
    message = ""
    for error in exc.errors():
        message += error['msg'] + f": {error['loc'][-1]}. "
    return returnError(400, message)

def HTTPExceptionHandler(_: Request, exc: HTTPException) -> JSONResponse:
    message = exc.detail if exc.detail else "unknown-error"
    if (exc.status_code == 404):
        message = 'not-found'
    return returnError(exc.status_code, message)

def ExceptionHandler(_: Request, exc: Exception) -> JSONResponse:

    print(f"ERROR: {str(exc)}")

    return returnError(500, 'internal-server-error')