import os
import sys

from dotenv import load_dotenv

from client.console.client import Client

if __name__ == '__main__':
    load_dotenv()
    server_host = os.environ['SERVER_HOST']
    server_port = int(os.environ['SERVER_PORT'])
    client_port = int(sys.argv[1])
    client = Client(server_host, client_port, server_port)
    client.start()
