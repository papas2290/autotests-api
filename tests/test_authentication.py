from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    public_user_client = get_public_users_client()
    authentication_user_client = get_authentication_client()

    create_user_request = CreateUserRequestSchema()
    create_user_response = public_user_client.create_user(request=create_user_request)
    print(f'create user response: {create_user_response}')

    login_request = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)

    login_response = authentication_user_client.login_api(request=login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    print(f'login response data: {login_response_data}')

    assert_status_code(actual=login_response.status_code, expected=HTTPStatus.OK)
    assert_login_response(response=login_response_data)

    validate_json_schema(instance=login_response.json(), schema=login_response_data.model_json_schema())
