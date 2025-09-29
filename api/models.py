import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator


#  В соответствии с тутором сделал такой regex, хоть я с ним и не согласен.
#  И считаю что имя пользователя должно храниться сугубо в формате никнэйма
#  (потом переделаю)
LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-z]+$")


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        from_attributes = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name must contain only letters"
            )
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Surname must contain only letters"
            )
        return value
