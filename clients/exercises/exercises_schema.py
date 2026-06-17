from pydantic import BaseModel, UUID4, Field, ConfigDict
from pydantic.alias_generators import to_camel
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """Описание структуры задания"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: UUID4
    title: str
    course_id: UUID4
    max_score: int | None
    min_score: int | None
    order_index: int
    description: str
    estimated_time: str


class GetExercisesQuerySchema(BaseModel):
    """Описание схемы запроса на получение списка заданий"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    course_id: UUID4


class GetExercisesResponseSchema(BaseModel):
    """Описание схемы ответа на получение списка заданий"""
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """Описание схемы запроса на создание задания"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    title: str = Field(default_factory=fake.sentence)
    course_id: UUID4 = Field(default_factory=fake.uuid4)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


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

    title: str = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    """Описание схемы ответа на обновление задания"""
    exercise: ExerciseSchema
