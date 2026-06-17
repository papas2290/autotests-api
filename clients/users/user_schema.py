from pydantic import BaseModel, ConfigDict, EmailStr, UUID4, Field
from pydantic.alias_generators import to_camel
from tools.fakers import fake


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

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)


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

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(default_factory=fake.last_name)
    first_name: str | None = Field(default_factory=fake.first_name)
    middle_name: str | None = Field(default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """Описание схемы ответа на обновление пользователя"""
    user: UserSchema
