
from Server.server import Server

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 2005
    server = Server(host, port)
    server.start()
