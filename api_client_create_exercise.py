from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

random_email = get_random_email()
name = random_email.split('@')[0]

public_user_client = get_public_users_client()

# User
create_user_request = CreateUserRequestSchema(
    email=random_email,
    password='123456',
    first_name=name,
    last_name=name,
    middle_name=name
)
create_user_response = public_user_client.create_user(request=create_user_request)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Клиенты
files_client = get_files_client(user=authentication_user)
course_client = get_courses_client(user=authentication_user)
exercise_client = get_exercises_client(user=authentication_user)

# Создание файла
create_file_request = CreateFileRequestSchema(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(request=create_file_request)
print(f'Create file data: {create_file_response}')

# Создание курса
create_course_request = CreateCourseRequestSchema(
    title='Python',
    maxScore=100,
    minScore=10,
    description='Практика использования API-клиентов',
    estimatedTime='2 weeks',
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = course_client.create_course(request=create_course_request)
print(f'Create course: {create_course_response}')

# Создание задания
create_exercise_request = CreateExerciseRequestSchema(
    title='Практика использования API-клиентов. Задание',
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    order_index=1,
    description='Создание задания',
    estimated_time='5 min'
)
create_exercise_response = exercise_client.create_exercise(request=create_exercise_request)
print(f'Create exercise Data: {create_exercise_response}')
