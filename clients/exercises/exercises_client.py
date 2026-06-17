from httpx import Response

from clients.api_client import ApiClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class Exercise(TypedDict):
    """Описание структуры задания"""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """Описание структуры запроса на получение списка заданий"""
    courseId: str


class GetExerciseResponseDict(TypedDict):
    """Описание структуры ответа на получение одного задания"""
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """Описание структуры ответа на получение списка заданий"""
    exercises: list[Exercise]


class CreateExerciseResponseDict(TypedDict):
    """Описание структуры ответа на создание задания"""


class CreateExerciseRequestDict(TypedDict):
    """Описание структуры запроса на создание задания"""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """Описание структуры запроса для обновления данных задания"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """Описание структуры ответа на обновление задания"""
    exercise: Exercise


class ExercisesClient(ApiClient):
    """Клиент для работы с /api/v1/exercises"""
    exercise: Exercise

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного задания
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id
        :param exercise_id: id задания
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание задания
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновление данных задания
        :param exercise_id: id задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.patch(f'/api/v1/exercise/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания
        :param exercise_id: id задания
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.delete(f'/api/v1/exercise/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получение одного задания по exercise_id
        :param exercise_id: id задания
        :return: Ответ в формате json
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получение списка заданий для определенного курса
        :param query: Словарь с courseId
        :return: Ответ в формате json
        """
        response = self.get_exercises_api(query=query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создание задания
        :param request: запрос на создание задания
        :return: Ответ в формате json
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Обновление задания
        :param exercise_id: id задания
        :param request: запрос на обновление задания
        :return: Ответ в формате json
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :param user: Словарь с email, password
    :return: Готовый клиент ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user=user))
