import httpx

from tools.fakers import fake

base_url = 'http://localhost:8000/api/v1/'

# создание пользователя
create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(url=f'{base_url}users', json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f'create user status code: {create_user_response.status_code}')

# авторизация
login_payload = {
    'email': create_user_payload['email'],
    'password': create_user_payload['password']
}

login_response = httpx.post(url='http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'login status code: {login_response.status_code}')

# Обновление пользователя
path_user_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
path_user_headers = {
    'Authorization': f'Bearer {login_response_data["token"]["accessToken"]}'
}
path_user_response = httpx.patch(
    url=f'{base_url}users/{create_user_response_data["user"]["id"]}',
    headers=path_user_headers,
    json=path_user_payload
)
print(f'path user status code: {path_user_response.status_code}')
