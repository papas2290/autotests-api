import pytest

from tools.allure.environment import create_allure_environment


@pytest.fixture(autouse=True, scope='session')
def save_allure_environment_file():
    yield
    create_allure_environment()