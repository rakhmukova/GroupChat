import json
import select
import socket
import sys

from past.builtins import raw_input

from Client.request_types import RequestType


def send_message(content):
    request = {
        'type': RequestType.SEND_MESSAGE.value,
        'content': content
    }
    return request


def set_username(name):
    request = {
        'type': RequestType.SET_USERNAME.value,
        'name': name
    }
    return request


class Client:
    def __init__(self, host, port, server_port):
        self.host = host
        self.port = port
        self.server_port = server_port
        self.client_socket = None

    def convert_and_send(self, data):
        to_send = json.dumps(data)
        self.client_socket.send(to_send.encode())

    def start(self):
        self.client_socket = socket.socket()
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.bind((self.host, self.port))
        self.client_socket.connect((self.host, self.server_port))
        name = input('Input your name: ')
        data = set_username(name)
        self.convert_and_send(data)

        while True:
            sockets = [self.client_socket, sys.stdin]
            ready_to_read, _, _ = select.select(sockets, [], [])
            for s in ready_to_read:
                if s == self.client_socket:
                    try:
                        data = s.recv(2048)
                        if not data:
                            print('\nDisconnected from server')
                            sys.exit()
                        message = json.loads(data)
                        print(f'<{message["sender_name"]}>: {message["content"]}')
                    except socket.error:
                        print("error!")
                else:
                    text = raw_input()
                    if text == "/exit":
                        break
                    data = send_message(text)
                    self.convert_and_send(data)
