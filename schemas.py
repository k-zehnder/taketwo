from pydantic import BaseModel, validator
import re


VALID_NAME_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
VALID_NAME_RANGE = [str(i) for i in range(3, 16)]


def is_valid_digits(query):
    matched = re.findall('\d+', query)
    return all(m in VALID_NAME_RANGE for m in matched)

def is_valid_chars(query):
    return all(char in VALID_NAME_CHARACTERS for char in query if char.isalpha())


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
