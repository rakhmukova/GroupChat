import json
from datetime import datetime
import socket
from _thread import *

from Server.message import Message


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connections = set()
        self.names = {}

    def handle_client(self, connection):
        data = connection.recv(2048)
        name = data.decode()
        if name:
            self.names[connection] = name
            while True:
                data = connection.recv(2048)
                content = data.decode()
                if not data:
                    break
                sender_name = self.names[connection]
                sending_time = datetime.now().strftime("%H:%M:%S")
                message = Message(content, sender_name, sending_time)
                self.broadcast(message, connection)
        connection.close()

    def broadcast(self, message, connection):
        json_data = json.dumps(message.__dict__)
        to_send = json_data.encode()
        broken_connections = set()
        for conn in self.connections:
            if conn != connection and connection in self.names:
                try:
                    conn.send(to_send)
                except Exception as e:
                    print(f"Connection with user {self.names[connection]} is broken")
                    conn.close()
                    broken_connections.add(conn)

        self.connections = self.connections.difference(broken_connections)

    def start(self):
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        print(f"Listening on port {self.port}...")
        while True:
            connection, address = server_socket.accept()
            print(f"Connected to {address}")
            self.connections.add(connection)
            start_new_thread(self.handle_client, (connection,))
