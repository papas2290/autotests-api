from pydantic import BaseModel, Field, EmailStr, ConfigDict, UUID4
from typing import Annotated
from pydantic.alias_generators import to_camel

EmailType = Annotated[EmailStr, Field(min_length=1, max_length=250)]  # строки с email
PasswordType = Annotated[str, Field(min_length=1, max_length=250)]  # строки с password
NameType = Annotated[str, Field(min_length=1, max_length=50)]  # строки с last_name, first_name, middle_name


class UserSchema(BaseModel):
    """Схема описания пользователя"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: UUID4
    email: EmailType
    last_name: NameType
    first_name: NameType
    middle_name: NameType


class CreateUserRequestSchema(BaseModel):
    """Схема описания запроса на создание пользователя"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    email: EmailType
    password: PasswordType
    last_name: NameType
    first_name: NameType
    middle_name: NameType


class CreateUserResponseSchema(BaseModel):
    """Схема описания ответа на создание пользователя"""
    user: UserSchema
