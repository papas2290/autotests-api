from typing import Self

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath


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
    allure_results_dir: DirectoryPath = DirectoryPath('allure-results')

    @classmethod
    def initialized(cls) -> Self:
        allure_results_dir = DirectoryPath('./allure-results')
        allure_results_dir.mkdir(exist_ok=True)

        return Settings(allure_results_dir=allure_results_dir)


settings = Settings.initialized()
