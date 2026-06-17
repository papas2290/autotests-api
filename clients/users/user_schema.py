from pydantic import BaseModel, ConfigDict, EmailStr, UUID4
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """Описание структуры схемы пользователя."""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: UUID4
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """Описание схемы запроса для создания пользователя. api/v1/users (POST)"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    email: str
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    """Описание схемы ответа создания пользователя."""
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """Описание схемы ответа получения пользователя."""
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание схемы запроса на обновление пользователя.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    email: EmailStr | None
    last_name: str | None
    first_name: str | None
    middle_name: str | None


class UpdateUserResponseSchema(BaseModel):
    """Описание схемы ответа на обновление пользователя"""
    user: UserSchema
