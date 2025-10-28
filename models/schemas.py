from dataclasses import dataclass
from pydantic import BaseModel

class UserRegister(BaseModel):
    fname: str
    lname: str
