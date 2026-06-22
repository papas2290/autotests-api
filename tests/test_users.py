import pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize('domain', ['mail.ru', 'gmail.com', 'example.com'])
def test_create_user(domain: str, public_users_client: PublicUsersClient):
    email = fake.email(domain=domain)
    request = CreateUserRequestSchema(email=email)
    response = public_users_client.create_user_api(request=request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_create_user_response(request=request, response=response_data)
    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client, function_user):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_get_user_response(get_user_response=response_data, create_user_response=function_user.response)
    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
