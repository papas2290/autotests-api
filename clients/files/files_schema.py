from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """Описание схемы файла."""
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """Описание схемы запроса на создание файла."""
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """Описание схемы ответа на создание файла."""
    file: FileSchema
