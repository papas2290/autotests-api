from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """Описание структуры пользователя."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """Описание структуры ответа создания пользователя."""
    user: User


class CreateUserRequestDict(TypedDict):
    """Описание запроса для создания пользователя. api/v1/users (POST)"""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(ApiClient):
    """Клиент для работы с api/v1/users"""

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание пользователя
        :param request: Запрос на создание пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.client.post(url='/api/v1/users', json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод создает пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в формате json
        """
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
