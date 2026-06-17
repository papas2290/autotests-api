from clients.api_client import ApiClient
from httpx import Response

from clients.public_http_builder import get_public_http_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(ApiClient):
    """Клиент для работы с api/v1/users"""

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание пользователя
        :param request: Запрос на создание пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.client.post(url='/api/v1/users', json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод создает пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в формате json
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
