import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    server_socket.settimeout(1.0)
    print(f'Сервер {server_address} запущен и ждет подключений...')

    list_msg = []

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue
            print(f'Подключение от {client_address}')

            msg = f'Пользователь с адресом: {client_address} отправил сообщение {client_socket.recv(1024).decode()}'
            print(msg)
            list_msg.append(msg)
            client_socket.send('\n'.join(list_msg).encode())
            client_socket.close()

    except KeyboardInterrupt:
        print(f'Сервер {server_address} остановлен')

    finally:
        server_socket.close()


if __name__ == '__main__':
    server()
