import httpx

login_payload = {
    "email": "anton@mail.ru",
    "password": "123456"
}
login_response = httpx.post(url='http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'login response: {login_response_data}')
print(f'status code login response: {login_response.status_code}')
print()

refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken']
}
refresh_response = httpx.post(url='http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print(f'refresh response: {refresh_response_data}')
print(f'status code refresh response: {refresh_response.status_code}')
