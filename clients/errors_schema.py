from typing import Any

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class ValidationErrorSchema(BaseModel):
    """Модель, описывающая структуру ошибки валидации API."""
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    type: str
    input: Any
    context: dict[str, Any] = Field(validation_alias='ctx')
    message: str = Field(validation_alias='msg')
    location: list[str] = Field(validation_alias='loc')


class ValidationErrorResponseSchema(BaseModel):
    """Модель, описывающая структуру ответа API с ошибкой валидации."""
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    details: list[ValidationErrorSchema] = Field(validation_alias='detail')


class InternalErrorResponseSchema(BaseModel):
    """Модель для описания внутренней ошибки."""
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    details: str = Field(validation_alias='detail')
