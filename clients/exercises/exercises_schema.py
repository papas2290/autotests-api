from typing import Annotated, Optional

from pydantic import BaseModel, UUID4, Field, ConfigDict
from pydantic.alias_generators import to_camel

TitleType = Annotated[str, Field(min_length=1, max_length=250)]  # поле title
OrderIndexType = Annotated[int, Field(default=0)]  # поле orderIndex
DescriptionType = Annotated[str, Field(min_length=1)]  # поле description
EstimatedTimeType = Annotated[Optional[str], Field(min_length=1, max_length=50)]  # поле estimatedTime


class ExerciseSchema(BaseModel):
    """Описание структуры задания"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: UUID4
    title: TitleType
    course_id: UUID4
    max_score: int | None
    min_score: int | None
    order_index: OrderIndexType
    description: DescriptionType
    estimatedTime: EstimatedTimeType


class GetExercisesQuerySchema(BaseModel):
    """Описание схемы запроса на получение списка заданий"""
    courseId: str


class GetExercisesResponseSchema(BaseModel):
    """Описание схемы ответа на получение списка заданий"""
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """Описание схемы запроса на создание задания"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    title: TitleType
    course_id: UUID4
    max_score: int | None
    min_score: int | None
    order_index: OrderIndexType
    description: DescriptionType
    estimated_time: EstimatedTimeType


class CreateExerciseResponseSchema(BaseModel):
    """Описание схемы ответа на создание задания"""
    exercise: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    """Описание схемы ответа на получение одного задания"""
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """Описание схемы запроса для обновления данных задания"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    title: TitleType
    max_score: int | None
    min_score: int | None
    orderIndex: OrderIndexType
    description: DescriptionType
    estimatedTime: EstimatedTimeType


class UpdateExerciseResponseSchema(BaseModel):
    """Описание схемы ответа на обновление задания"""
    exercise: ExerciseSchema
