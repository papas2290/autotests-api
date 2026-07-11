from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath


class HttpClientConfig(BaseModel):
    """Описание настроек для клиента http"""
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        """Возвращает URL в виде строки.

        Преобразует поле url (HttpUrl) в строковый формат для удобного
        использования в HTTP-запросах.

        :return str: Строковое представление URL.
        """
        return str(self.url)


class TestDataConfig(BaseModel):
    """Описание настроек для тестовых данных"""
    image_png_file: FilePath


class Settings(BaseSettings):
    """Общие настройки для проекта"""
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    test_data: TestDataConfig
    http_client: HttpClientConfig


settings = Settings()
