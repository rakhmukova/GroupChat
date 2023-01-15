import sys

from Client.Console.client import Client

if __name__ == '__main__':
    host = '127.0.0.1'
    port = int(sys.argv[1])
    server_port = 2005
    client = Client(host, port, server_port)
    client.start()
