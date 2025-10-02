from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints


class CreateUser(BaseModel):
    username: Annotated[str, StringConstraints(min_length=3, max_length=25)]
    email: EmailStr
