import random
import socket
import abc
import sys
import asyncio
from tkinter import *
import time
import datetime
from typing import Callable
import threading


# class Socket(abc.ABC):
#     def __init__(self):
#         self.socket = socket.socket(
#             socket.AF_INET,
#             socket.SOCK_STREAM,
#         )
#         # Создается цикл событий
#         # Специальный цикл, в котором все функции выполняются асинхронно
#         self.main_loop = asyncio.new_event_loop()
#
#     # Метод для отправки данных
#     @abc.abstractmethod
#     async def send_data(self):
#         raise NotImplementedError()
#
#     # Метод для получения данных
#     @abc.abstractmethod
#     async def listen_socket(self):
#         raise NotImplementedError()
#
#     # Метод для настройки начальных значений
#     @abc.abstractmethod
#     def set_up(self):
#         raise NotImplementedError()
#
#     # Основной метод работы
#     @abc.abstractmethod
#     async def main(self):
#         raise NotImplementedError()
#
#     # Запускает метод main в асинхронном режиме
#     def start(self):
#         try:
#             return self.main_loop.run_until_complete(self.main())
#         except Exception as e:
#             self.main_loop.close()
#             self.main_loop.stop()


class Client:
    def __init__(self, host, port):
        # super(Client, self).__init__()
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.main_loop = asyncio.new_event_loop()
        self.socket.settimeout(2)

        self.host = host
        self.port = port
        # Адрес сервера, к которому мы будем подключаться
        self.address = self.host, self.port
        # Размер пакета в байтах, который мы будем считывать
        self.size = 1024
        # Флаг, символизирующий есть ли подключение у клиента к серверу
        self.success_connect = False
        self.msg = '123'

    # async def send_data(self):
    #     # Метод отправляет асинхронно строчку data и после отправки закрывает цикл событий
    #     data = "sss"
    #     # await - это как return только в асинхронной функции
    #     await self.main_loop.sock_sendall(self.socket, data.encode("utf-8"))
    #     self.main_loop.close()

    async def listen_socket(self, listened_socket=None):
        try:
            # Пытаюсь получить данные
            #data = self.socket.recv(1024)
            data = await self.main_loop.sock_recv(self.socket, 1024)
            #print(data)
            if data:
                # TODO поправить отправку с сервера
                self.msg = data.decode("utf-8")
                print(self.msg)
            self.shut_down_main_loop()
        except ConnectionResetError:
            print(f"Соединение по адресу {self.address} разорвано")
            # Если соединение разорвано, то закрываем сокет и цикл событий
            self.shut_down_main_loop()


    def shut_down_main_loop(self):
        # Метод, который завершает работу цикла событий
        self.socket.close()
        try:
            self.socket.close()
        except Exception:
            pass

    def set_up(self):
        try:
            # Устанавливаем соединение с сервером
            self.socket.connect(self.address)
            # Флаг поставим в позицию True
            self.success_connect = True
            print(f"Успешное подключение к серверу {self.address}")
        except ConnectionRefusedError:
            # Флаг поставим в позицию False
            self.success_connect = False
            print(f"Сервер по адресу {self.address} не отвечает")
        except socket.error:
            print(f"Сервер по адресу {self.address} не отвечает")
            self.socket.close()
       # self.socket.setblocking(True)

    def start(self):
        #self.listen_socket()
        try:
            return self.main_loop.run_until_complete(self.listen_socket())
        except Exception as e:
            self.main_loop.close()
            self.main_loop.stop()

    # def main(self):
    #     # Объединяю асинхронные методы для чтения\записи с сервера в одну задачу
    #     # await asyncio.gather(
    #     #     self.main_loop.create_task(self.listen_socket()),
    #     #     self.main_loop.create_task(self.send_data()),
    #     # )
    #     # self.socket.close()


class Painter:
    def __init__(self, canvas) -> object:
        self.canvas: Tk = canvas

    def add_element(self, x, y, action: Callable, **kwargs):
        element = action(self.canvas, **kwargs)
        element.place(x=x, y=y)
        return element

    def add_button(self, x, y, **kwargs):
        # Метод для создания кнопки
        return self.add_element(x, y, action=Button, **kwargs)

    def add_label(self, x, y, **kwargs):
        # Метод для создания лэйбла
        return self.add_element(x, y, action=Label, **kwargs)


class Task:
    def __init__(self, window, element, host, port, seconds, func):
        self.window = window
        self.element = element
        self.host = host
        self.port = port
        self.seconds = seconds
        self.ms = self.seconds * 1000

    def run(self):
        self.__run()


class Application:
    def __init__(self, addresses):
        self.addresses = addresses if isinstance(addresses, dict) else None
        if not self.addresses:
            raise Exception("Неверно введены настройки маршрутизации")
            sys.exit(1)
        self.window = Tk()
        self.window.title('ГМ "ОКЕЙ" Шварца 15')
        self.window.geometry('1920x1080')
        self.painter = Painter(canvas=self.window)
        self.main_loop = asyncio.new_event_loop()

    def set_up(self):
        # В этом методе отрисовываются все графические элементы перед
        # стартом обновления окошка
        self.clock = self.painter.add_label(x=1580, y=20,
                                            text='pysk',
                                            foreground='#964b00',
                                            font=('Helvetica', 20),
                                            pady=5)

        self.humidity_label = self.painter.add_label(x=50, y=40,
                                                     text='КНС'.center(26),
                                                     foreground='green',
                                                     background='white',
                                                     pady=15,
                                                     font=('Helvetica', 20),
                                                     borderwidth=2)

        self.humidity_label2 = self.painter.add_label(x=140, y=40,
                                                     text='22'.center(26),
                                                     foreground='green',
                                                     background='white',
                                                     pady=15,
                                                     font=('Helvetica', 20),
                                                     borderwidth=2)

        self.humidity_label3 = self.painter.add_label(x=240, y=40,
                                                      text='22'.center(26),
                                                      foreground='green',
                                                      background='white',
                                                      pady=15,
                                                      font=('Helvetica', 20),
                                                      borderwidth=2)

        self.devices = {
            1: self.humidity_label
        }

    def __run(self, host, port):
        # TODO переделать в синхронное программирование
        client_socket = Client(host=host, port=port)
        client_socket.set_up()
        if client_socket.success_connect:
            client_socket.start()
            return client_socket.msg
        # self.window.update_idletasks()
        # self.window.after(self.seconds, self.run)

    @staticmethod
    def task(seconds, host=None, port=None):
        def inner_decorator(func):
            def wrapper(self, *args, **kwargs):
                if host and port:
                    msg = self.__run(host, port)
                    func(self, seconds, msg)
                else:
                    func(self, seconds)

               # self.window.update_idletasks()
              #  self.window.after(seconds * 1000, func, self, seconds * 1000)
            return wrapper

        return inner_decorator

    def update(self):
        self.update_clock()
        self.update_label1()
        self.update_label2()
        self.update_label3()
        self.window.mainloop()

    @task(seconds=1)
    def update_clock(self, seconds):
        self.clock['text'] = time.ctime()[10:20]
        self.clock['text'] = datetime.date.today().strftime(
            "%d-%m-%Y") + '  ' + time.ctime()[10:20]
        self.window.update_idletasks()
        self.window.after(seconds*1000, self.update_clock)

    @task(seconds=5, host='127.0.0.1', port=8080)
    def update_label1(self, seconds, msg):
        self.humidity_label['text'] = msg
        self.window.update_idletasks()
        self.window.after(seconds*1000, self.update_label1)

    @task(seconds=10, host='127.0.0.2', port=8080)
    def update_label2(self, seconds, msg):
        self.humidity_label2['text'] = msg
        self.window.update_idletasks()
        self.window.after(seconds * 1000, self.update_label2)

    @task(seconds=2, host='127.0.0.3', port=8080)
    def update_label3(self, seconds, msg):
        self.humidity_label3['text'] = msg
        if int(self.humidity_label3['text']) > 50:
            self.humidity_label3['background'] = 'red'
        else:
            self.humidity_label3['background'] = 'white'
        self.window.update_idletasks()
        self.window.after(seconds * 1000, self.update_label3)


if __name__ == "__main__":
    # IP устройства и его уникальный номер
    # Если надо передать пару "хост:порт", то можно передать её так:
    # {1: ('127.0.0.1', 8080), 2: ('127.0.0.2', 8090)}
    addresses = {
        1: '127.0.0.1',
        2: '127.0.0.2',
        3: '127.0.0.3',
        4: '127.0.0.4',
        5: '127.0.0.5',

    }
    app = Application(addresses=addresses)
    app.set_up()
    app.update()
    # app.update()
    # app.start_main()
