
from pydantic import BaseModel, validator


class Tag(BaseModel):
    name: str
    value: int

    @validator("name")
    def is_valid_name(cls, name):
        print(is_valid_digits(name))
        valid_digits = is_valid_digits(name)
        if not valid_digits:
             raise ValueError("Bad name, digits are {3, 15}.") 
        valid_chars = is_valid_chars(name)      
        if not valid_chars:
            raise ValueError("Bad name, must be character.")
        return name

    @validator("value")
    def is_valid_value(cls, value):
        """Validator to check whether value is valid"""
        if not 0 <= value < 10:
            raise ValueError("Bad value, must be integer and 0 <= integer < 10")
        return value

    class Config:
        orm_mode = True
