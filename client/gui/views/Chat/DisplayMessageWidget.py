from PyQt6.QtWidgets import *

import os


class DisplayMessageWidget(QWidget):
    def __init__(self, sender_name, message_content):
        super(DisplayMessageWidget, self).__init__()

        self.setObjectName('messageWidget')

        self.layout = QVBoxLayout(self)

        self.sender_label = QLabel(self)
        self.sender_label.setText(sender_name)
        self.sender_label.setObjectName('senderLabel')

        self.message_label = QLabel(self)
        self.message_label.setText(message_content)
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName('messageLabel')

        self.layout.addWidget(self.sender_label)
        self.layout.addWidget(self.message_label)

        print(os.getcwd())