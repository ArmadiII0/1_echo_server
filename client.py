import socket

def connect_to_server():
    global sock
    sock = socket.socket()
    sock.connect(('localhost', 9092))
    print("Успешно подключено к серверу.")

def receive_data():
    try:
        data = sock.recv(1024)
        print('Прием данных от сервера:', data.decode())
    except socket.error as e:
        print(f"Ошибка при получении данных: {e}")

def send_data():
    try:
        message = input("Введите сообщение для отправки на сервер: ")
        print('Отправка данных серверу:', message)
        sock.sendall(message.encode())
    except socket.error as e:
        print(f"Ошибка при отправке данных: {e}")

def disconnect_from_server():
    try:
        sock.close()
        print('Отключение от сервера')
    except socket.error as e:
        print(f"Ошибка при отключении: {e}")

def ex():
    exit()

options = {
    '1': connect_to_server,
    '2': receive_data,
    '3': send_data,
    '4': disconnect_from_server,
    '5': ex
}

while True:
    print("Меню:")
    print("1. Подключиться к серверу")
    print("2. Получить данные от сервера")
    print("3. Отправить данные серверу")
    print("4. Отключиться от сервера")
    print("5. Завершить программу")
    choice = input("Выберите действие: ")

    if choice in options:
        options[choice]()
    else:
        print("Неверный выбор. Пожалуйста, введите корректное значение.")
