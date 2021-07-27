class ApiError(Exception):
    codes = {
        'badRequest': 400,
        'notAuthorized': 401,
        'notFound': 404,
        'serverError': 500,
        'dependencyError': 502,
        'dependencyTimout': 504
    }
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    @classmethod
    def badRequest(cl, message : str): 
        return ApiError(ApiError.codes['badRequest'], message)

    @classmethod
    def notAuthorized(cl, message : str):
        return ApiError(ApiError.codes['notAuthorized'], message)

    @classmethod
    def notFound(cl, message : str):
        return ApiError(ApiError.codes['notFound'], message)
    
    @classmethod
    def dependencyError(cl, message : str):
        return ApiError(ApiError.codes['dependencyError'], message)
    
    @classmethod
    def dependencyTimeout(cl, message : str):
        return ApiError(ApiError.codes['dependencyTimeout'], message)
    
    @classmethod
    def serverError(cl, message : str):
        return ApiError(ApiError.codes['serverError'], message)
    