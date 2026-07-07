import allure
from httpx import Response

from clients.api_client import ApiClient

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExerciseResponseSchema, \
    GetExercisesResponseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema


class ExercisesClient(ApiClient):
    """Клиент для работы с /api/v1/exercises"""

    @allure.step('Get exercises')
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получение списка заданий для определенного задания
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get('/api/v1/exercises', params=query.model_dump(by_alias=True, mode='json'))

    @allure.step('Get exercise by id {exercise_id}')
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id
        :param exercise_id: id задания
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    @allure.step('Create exercise')
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание задания
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post('/api/v1/exercises', json=request.model_dump(by_alias=True, mode='json'))

    @allure.step('Update exercise by id {exercise_id}')
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновление данных задания
        :param exercise_id: id задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True, mode='json'))

    @allure.step('Delete exercise by id {exercise_id}')
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания
        :param exercise_id: id задания
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получение одного задания по exercise_id
        :param exercise_id: id задания
        :return: Ответ в формате json
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получение списка заданий для определенного курса
        :param query: Словарь с courseId
        :return: Ответ в формате json
        """
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создание задания
        :param request: запрос на создание задания
        :return: Ответ в формате json
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Обновление задания
        :param exercise_id: id задания
        :param request: запрос на обновление задания
        :return: Ответ в формате json
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :param user: Словарь с email, password
    :return: Готовый клиент ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user=user))
