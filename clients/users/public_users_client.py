from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict


class CreateUserDict(TypedDict):
    """Описание запроса для создания пользователя. api/v1/users (POST)"""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(ApiClient):
    """Клиент для работы с api/v1/users"""

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Создание пользователя
        :param request: Запрос на создание пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.client.post(url='/api/v1/users', json=request)
