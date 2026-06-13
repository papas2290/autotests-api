import httpx

base_url = 'http://localhost:8000/api/v1/'

payload_login = {
    "email": "anton@mail.ru",
    "password": "123456"
}

response_login = httpx.post(url=f'{base_url}authentication/login', json=payload_login)
response_login_json = response_login.json()
access_token = response_login_json['token']['accessToken']
print(f'status code login: {response_login.status_code}')
print(f'access token login: {access_token}')
print()

headers_user_me = {'Authorization': f'Bearer {access_token}'}
response_user_me = httpx.get(url=f'{base_url}users/me', headers=headers_user_me)
print(f'Ответ от user/me: {response_user_me.json()}')
print(f'Статус код от user/me: {response_user_me.status_code}')
