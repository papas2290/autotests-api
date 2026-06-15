from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

random_email = get_random_email()
name = random_email.split('@')[0]

public_user_client = get_public_users_client()

# User
create_user_request = CreateUserRequestDict(
    email=random_email,
    password='123456',
    lastName=name,
    firstName=name,
    middleName=name
)
create_user_response = public_user_client.create_user(request=create_user_request)
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# Клиенты
files_client = get_files_client(user=authentication_user)
course_client = get_courses_client(user=authentication_user)
exercise_client = get_exercises_client(user=authentication_user)

# Создание файла
create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(request=create_file_request)
print(f'Create file data: {create_file_response}')

# Создание курса
create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description='Практика использования API-клиентов',
    estimatedTime='2 weeks',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(request=create_course_request)
print(f'Create course: {create_course_response}')

# Создание задания
create_exercise_request = CreateExerciseRequestDict(
    title='Практика использования API-клиентов. Задание',
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=1,
    description='Создание задания',
    estimatedTime='5 min'
)
create_exercise_response = exercise_client.create_exercise(request=create_exercise_request)
print(f'Create exercise Data: {create_exercise_response}')
