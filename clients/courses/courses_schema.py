from pydantic import BaseModel, UUID4, Field
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema, ConfigDict
from typing import Annotated, Optional

TitleType = Annotated[str, Field(min_length=1, max_length=250)]
DescriptionType = Annotated[str, Field(min_length=1)]
EstimatedTimeType = Annotated[Optional[str], Field(min_length=1, max_length=50)]


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
    previewFile: FileSchema
    estimatedTime: EstimatedTimeType
    createdByUser: UserSchema


class GetCoursesQuerySchema(BaseModel):
    """Описание схемы запроса на получение списка курсов."""
    user_id: UUID4 = Field(alias='userId')


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
    maxScore: int | None
    minScore: int | None
    description: DescriptionType
    estimatedTime: EstimatedTimeType
    previewFileId: UUID4
    createdByUserId: UUID4


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
    maxScore: int | None
    minScore: int | None
    description: DescriptionType
    estimatedTime: EstimatedTimeType


class UpdateCourseResponseSchema(BaseModel):
    """Описание схемы ответа на обновление курса"""
    course: CourseSchema
