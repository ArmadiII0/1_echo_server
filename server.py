import socket

def create_socket_and_listen():
    global sock, conn, addr
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(0)
    print('Начало прослушивания порта')
    conn, addr = sock.accept()
    print('Подключение клиента', addr)

def receive_data_from_client():
    try:
        data = conn.recv(1024)
        print('Прием данных от клиента:', data.decode())
    except socket.error as e:
        print(f"Ошибка при получении данных: {e}")

def send_data_to_client():
    try:
        message = input("Введите сообщение для клиента: ")
        conn.sendall(message.encode())
        print('Отправка данных клиенту:', message)
    except socket.error as e:
        print(f"Ошибка при отправке данных: {e}")

def disconnect_client():
    try:
        conn.close()
        print('Отключение клиента', addr)
    except socket.error as e:
        print(f"Ошибка при отключении: {e}")

def ex():
    exit()

options = {
    '1': create_socket_and_listen,
    '2': receive_data_from_client,
    '3': send_data_to_client,
    '4': disconnect_client,
    '5': ex
}

while True:
    print("Меню:")
    print("1. Создать сокет и начать прослушивание")
    print("2. Получить данные от клиента")
    print("3. Отправить данные клиенту")
    print("4. Отключить клиента")
    print("5. Завершить программу")
    choice = input("Выберите действие: ")

    if choice in options:
        options[choice]()
    else:
        print("Неверный выбор. Пожалуйста, введите корректное значение.")
