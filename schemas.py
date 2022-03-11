from fastapi.responses import JSONResponse
import re
from typing import List
from pydantic import BaseModel, validator
from config import VALID_NAME_CHARACTERS, VALID_NAME_RANGE


class Tag(BaseModel):
    name: str
    value: int = 0

    class Config:
        orm_mode = True
        schema_extra = {
            "example" : {
                "name" : "init_foo",
                "value" : 0
            }
        }

class TagCreate(Tag):
    @validator("name")
    def is_valid_name(cls, name: str):
        valid_chars = is_valid_chars(name)   
        if not valid_chars:  
            raise IsValidCharsError(value=valid_chars, message="[a-z_] required")
        
        valid_digits = is_valid_digits(name)
        if not valid_digits:
            raise IsValidDigitsError(value=valid_digits, message="{3,15} required.")
        return name

    @validator("value")
    def is_valid_value(cls, value: int):
        valid_value = is_valid_value(value)   
        if not valid_value:
            raise IsValidValueError(value=valid_value, message="0 <= value < 10 required.")
        return value  

class TagRead(BaseModel):
    data: List[Tag]


def is_valid_digits(query: str) -> bool:
    matched = re.findall('\d+', query)
    return all(m in VALID_NAME_RANGE for m in matched)

def is_valid_chars(query: str) -> bool:
    return all(char in VALID_NAME_CHARACTERS for char in query if char.isalpha())

def is_valid_value(value: int) -> bool:
    return 0 <= value < 10

class IsValidCharsError(Exception):
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class IsValidDigitsError(Exception):
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class IsValidValueError(Exception):
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

def ErrorResponseModel(code, message):
    return JSONResponse(
        status_code=code, 
        content={"code": code, "message": message}
    )