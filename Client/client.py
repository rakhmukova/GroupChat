import json
import select
import socket
import sys

from past.builtins import raw_input


class Client:
    def __init__(self, host, port, server_port):
        self.host = host
        self.port = port
        self.server_port = server_port

    def start(self):
        client_socket = socket.socket()
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client_socket.bind((self.host, self.port))
        client_socket.connect((self.host, self.server_port))
        name = input('Input your name: ')
        client_socket.send(name.encode())

        while True:
            sockets = [client_socket, sys.stdin]
            ready_to_read, _, _ = select.select(sockets, [], [])
            for s in ready_to_read:
                if s == client_socket:
                    try:
                        data = s.recv(2048)
                        if not data:
                            print('\nDisconnected from server')
                            sys.exit()
                        message = json.loads(data)
                        print(f'<{message["sender_name"]}>: {message["content"]}')
                    except socket.error:
                        print("error!")
                    break
                else:
                    text = raw_input()
                    if text == "/exit":
                        break
                    client_socket.send(text.encode())