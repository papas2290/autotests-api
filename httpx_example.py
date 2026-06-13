import httpx

from httpx import request

response = httpx.get(url='https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())

data = {
    'title': 'Новая задача',
    'completed': False,
    'userId': 1
}

response = httpx.post(url='https://jsonplaceholder.typicode.com/todos', json=data)

print(response.status_code)
print(response.json())

data = {'username': 'test_user', 'password': '123456'}
response = httpx.post(url='https://httpbin.org/post', data=data)
print(response.status_code)
print(response.json())

headers = {'Authorization': 'Bearer my_secret_token'}
response = httpx.get(url='https://httpbin.org/post', headers=headers)
print(response.request.headers)
print(response.status_code)
print(response.json())

params = {'userId': 1}
response = httpx.get(url='https://jsonplaceholder.typicode.com/todos', params=params)
print(response.url)
print(response.json())

files = {'file': ('example.txt', 'rb')}
response = httpx.post(url='https://httpbin.org/post', files=files)
print(response.json())

with httpx.Client() as client:
    response_1 = client.get(url='https://jsonplaceholder.typicode.com/todos/1')
    response_2 = client.get(url='https://jsonplaceholder.typicode.com/todos/2')

print(response_1.json())
print(response_2.json())

client = httpx.Client(headers={'Authorization': 'Bearer my_secret_token'})
response = client.get('https://httpbin.org/post')
print(response.json())

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid-url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса: {e}')

try:
    response = httpx.get(url='https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout:
    print('Запрос превысил лимит времени')
