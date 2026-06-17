from pydantic import BaseModel, UUID4, Field, ConfigDict
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema
from typing import Annotated, Optional

TitleType = Annotated[str, Field(min_length=1, max_length=250)]
DescriptionType = Annotated[str, Field(min_length=1)]
EstimatedTimeType = Optional[Annotated[str, Field(min_length=1, max_length=50)]]


class CourseSchema(BaseModel):
    """Описание схемы курса"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: UUID4
    title: TitleType
    max_score: int | None
    min_score: int | None
    description: DescriptionType
    preview_file: FileSchema
    estimated_time: EstimatedTimeType
    created_by_user: UserSchema


class GetCoursesQuerySchema(BaseModel):
    """Описание схемы запроса на получение списка курсов."""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    user_id: UUID4


class GetCoursesResponseSchema(BaseModel):
    """Описание схемы ответа на получение списка курсов"""
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """Описание схемы запроса на создание курса."""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    title: TitleType
    max_score: int | None
    min_score: int | None
    description: DescriptionType
    estimated_time: EstimatedTimeType
    preview_file_id: UUID4
    created_by_user_id: UUID4


class CreateCourseResponseSchema(BaseModel):
    """Описание схемы ответа на создание курса"""
    course: CourseSchema


class GetCourseResponseSchema(BaseModel):
    """Описание схемы ответа на получение одного курса"""
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """Описание схемы запроса на обновление курса."""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    title: TitleType
    max_score: int | None
    min_score: int | None
    description: DescriptionType
    estimated_time: EstimatedTimeType


class UpdateCourseResponseSchema(BaseModel):
    """Описание схемы ответа на обновление курса"""
    course: CourseSchema
