import json
import socket
import sys

from PyQt6.QtCore import QObject, pyqtSignal

from client.gui.models.MockSocket import MockSocket
from client.console.client import send_message, set_username


class ModelClient(QObject):
    message_received = pyqtSignal(str, str)
    login_required = pyqtSignal()
    name_set = pyqtSignal(str)

    def __init__(self, server_host, client_port, server_port):
        super(ModelClient, self).__init__()

        self.server_host = server_host
        self.server_port = server_port
        self.client_host = '127.0.0.1'
        self.client_port = client_port
        self.client_socket = None

    def convert_and_send(self, data):
        to_send = json.dumps(data)
        self.client_socket.send(to_send.encode())

    def send_message(self, text):
        data = send_message(text)
        self.convert_and_send(data)

    def set_username(self, name):
        data = set_username(name)
        self.convert_and_send(data)
        # wait for a response
        self.name_set.emit(name)

    def run(self):
        self.client_socket = socket.socket()  # MockSocket()
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.bind((self.client_host, self.client_port))
        self.client_socket.connect((self.server_host, self.server_port))

        while True:
            data = self.client_socket.recv(2048)
            if not data:
                print('\nDisconnected from server')
                sys.exit()
            message = json.loads(data.decode())
            sender = message['sender_name']
            content = message['content']
            self.message_received.emit(sender, content)
