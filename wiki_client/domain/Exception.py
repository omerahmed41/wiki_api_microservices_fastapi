from fastapi import HTTPException


class DomainException(HTTPException):
    def __init__(self, name: str, status_code, detail):
        self.name = name
        self.status_code = status_code
        self.detail = detail

