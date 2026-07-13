from config import settings
import platform
import sys


def create_allure_environment_file():
    """
    Создаёт файл environment.properties для Allure отчёта.

    Функция собирает все настройки из объекта `settings` (pydantic-модель),
    сериализует их в формат `ключ=значение` и записывает в файл
    `environment.properties` в директории, указанной в `settings.allure_results_dir`.

    Этот файл используется Allure Framework для отображения информации
    об окружении (браузер, версия, base URL и т.д.) в финальном отчёте.

    Returns:
        None
    """
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items.append(f'os_info={platform.version()}, {platform.release()}')
    items.append(f'python_version={sys.version}')
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
