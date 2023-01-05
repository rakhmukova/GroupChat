from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QTextEdit, QSizePolicy


class SendMessageWidget(QTextEdit):
    send_message = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.handle_change)
        self.setObjectName('sendMessage')

        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setSizePolicy(size_policy)

    def handle_change(self):
        if not self.toPlainText().endswith("\n"):
            return

        if QApplication.keyboardModifiers() and Qt.Modifier.SHIFT:
            return

        message = self.toPlainText()
        self.clear()
        self.send_message.emit(message)
