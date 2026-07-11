from pydantic import BaseModel, HttpUrl, Field, UUID4, FilePath
from tools.fakers import fake


class FileSchema(BaseModel):
    """Описание схемы файла."""
    id: UUID4
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """Описание схемы запроса на создание файла."""
    filename: str = Field(default_factory=lambda: f'{fake.uuid4()}.png')
    directory: str = Field(default='tests')
    upload_file: FilePath


class CreateFileResponseSchema(BaseModel):
    """Описание схемы ответа на создание файла."""
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """Описание схемы ответа на получение файла"""
    file: FileSchema
