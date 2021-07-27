from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union, List, Type
from fastapi.encoders import jsonable_encoder

def succesfulResponse(code : int, data : Union[BaseModel, List[BaseModel], None]) -> JSONResponse: 
    response = {
        'status': 'success',
        'data' : data
    }
    json_response = jsonable_encoder(response)
    return JSONResponse(content=json_response, status_code=code)