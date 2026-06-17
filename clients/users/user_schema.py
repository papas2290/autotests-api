from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserSchema(BaseModel):
    """Описание структуры схемы пользователя."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """Описание схемы запроса для создания пользователя. api/v1/users (POST)"""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


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
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias='lastName')
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')


class UpdateUserResponseSchema(BaseModel):
    """Описание схемы ответа на обновление пользователя"""
    user: UserSchema
