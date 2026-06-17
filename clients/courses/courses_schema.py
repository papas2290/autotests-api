from pydantic import BaseModel, UUID4, Field, ConfigDict
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema
from typing import Annotated, Optional
from tools.fakers import fake


class CourseSchema(BaseModel):
    """Описание схемы курса"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: UUID4
    title: str = Field(min_length=1, max_length=250)
    max_score: int | None
    min_score: int | None
    description: str
    preview_file: FileSchema
    estimated_time: Optional[str]
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

    title: str = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: Optional[str] = Field(default_factory=fake.estimated_time)
    preview_file_id: UUID4 = Field(default_factory=fake.uuid4)
    created_by_user_id: UUID4 = Field(default_factory=fake.uuid4)


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

    title: str = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: Optional[str] = Field(default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    """Описание схемы ответа на обновление курса"""
    course: CourseSchema
