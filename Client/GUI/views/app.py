import os
import sys

from dotenv import load_dotenv

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication

from Client.GUI.views.Chat.ChatWindow import ChatWindow
from Client.GUI.views.Login.LoginWindow import LoginWindow
from Client.GUI.models.ModelClient import ModelClient


class App(QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.chat_window = None
        load_dotenv()
        server_host = os.environ['SERVER_HOST']
        server_port = int(os.environ['SERVER_PORT'])
        client_port = int(sys.argv[1])

        self.thread = QThread()
        self.thread.start()

        self.model = ModelClient(server_host, client_port, server_port)
        self.model_thread = QThread()
        self.model.moveToThread(self.model_thread)
        self.model_thread.started.connect(self.model.run)
        self.model_thread.start()

        self.lastWindowClosed.connect(self.stop_thread)

        self.login_window = LoginWindow(self.model)
        self.login_window.setGeometry(300, 200, 600, 400)
        self.login_window.show()

        self.model.name_set.connect(self.enter_chat)

        qss_file = open('views/style.qss').read()
        self.setStyleSheet(qss_file)

    def enter_chat(self, name):
        geometry = self.login_window.geometry()
        self.login_window.close()
        self.chat_window = ChatWindow(self.model, name, geometry)
        self.chat_window.show()

    def stop_thread(self):
        self.model_thread.exit()
        self.thread.exit()
        self.thread.wait()
