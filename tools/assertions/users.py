import allure

from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


@allure.step('Check create user response')
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema) -> None:
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=response.user.email, expected=request.email, name='email')
    assert_equal(actual=response.user.last_name, expected=request.last_name, name='last_name')
    assert_equal(actual=response.user.first_name, expected=request.first_name, name='last_name')
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name='middle_name')


@allure.step('Check user')
def assert_user(actual: UserSchema, expected: UserSchema) -> None:
    """
    Проверяет корректность данных пользователя
    :param actual: Актуальные данные в виде схемы UserSchema
    :param expected: Ожидаемые данные в виде схемы UserSchema
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    assert_equal(actual=actual.id, expected=expected.id, name='id')
    assert_equal(actual=actual.email, expected=expected.email, name='email')
    assert_equal(actual=actual.last_name, expected=expected.last_name, name='last_name')
    assert_equal(actual=actual.first_name, expected=expected.first_name, name='first_name')
    assert_equal(actual=actual.middle_name, expected=expected.middle_name, name='middle_name')


@allure.step('Check GET user response')
def assert_get_user_response(get_user_response: GetUserResponseSchema,
                             create_user_response: CreateUserResponseSchema) -> None:
    """
    Проверяет, что данные пользователя при создании и при запросе совпадают
    :param get_user_response: ответ API при запросе пользователя
    :param create_user_response: ответ API при создании пользователя
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    assert_user(actual=get_user_response.user, expected=create_user_response.user)
