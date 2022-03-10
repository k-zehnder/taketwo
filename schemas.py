from pydantic import BaseModel, validator
import re


VALID_NAME_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz' 
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
        valid_chars = is_valid_chars(name)   
        if not valid_chars:  
            raise ValueError("Invalid chars")  
        valid_digits = is_valid_digits(name)
        if not valid_digits:
             raise ValueError("Invalid digits") 
        return name

    class Config:
        orm_mode = True
