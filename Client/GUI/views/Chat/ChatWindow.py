from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import *

from Client.GUI.views.Chat.DisplayMessagesArea import DisplayMessagesArea
from Client.GUI.views.Chat.SendMessageWidget import SendMessageWidget


class ChatWindow(QDialog):
    def __init__(self, model, name, geometry):
        super(ChatWindow, self).__init__()

        self.setWindowTitle('Chat')
        self.setGeometry(geometry)

        self.display_messages_area = None
        self.send_message_widget = None
        self.scroll_layout = None
        self.username = name

        self._model = model
        self._model.message_received.connect(self.on_new_message_received)

        self.init_chat()

    @pyqtSlot(str, str)
    def on_new_message_received(self, sender, content):
        self.display_messages_area.update_chat(sender, content)

    def scroll_down(self):
        vbar = self.display_messages_area.verticalScrollBar()
        vbar.setValue(vbar.maximum())

    def init_chat(self):
        box_layout = QVBoxLayout(self)
        box_layout.setObjectName('chatLayout')
        self.setLayout(box_layout)

        self.display_messages_area = DisplayMessagesArea()
        self.send_message_widget = SendMessageWidget()
        self.send_message_widget.send_message.connect(self.send_message)

        box_layout.addWidget(self.display_messages_area, stretch=7)
        box_layout.addWidget(self.send_message_widget, stretch=1)

        self.scroll_down()

    def send_message(self, message):
        self._model.send_message(message)
        self.display_messages_area.update_chat(self.username, message)
