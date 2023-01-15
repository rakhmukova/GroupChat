import os
from dotenv import load_dotenv
from Server.server import Server

if __name__ == '__main__':
    load_dotenv()
    host = os.environ['SERVER_HOST']
    port = int(os.environ['SERVER_PORT'])
    server = Server(host, port)
    server.start()
