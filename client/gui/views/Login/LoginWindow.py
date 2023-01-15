from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class LoginWindow(QDialog):
    def __init__(self, model):
        super(LoginWindow, self).__init__()
        self._model = model

        self.setWindowTitle('Login')

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        form_layout = QFormLayout()

        self.username_label = QLabel('Username:')
        self.username_label.setObjectName('labelUserName')

        self.username_edit = QLineEdit()
        self.username_edit.setObjectName('lineEditUserName')
        self.username_edit.setFixedSize(200, 25)

        username_layout = QHBoxLayout()
        username_layout.addWidget(self.username_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        form_layout.addRow(self.username_label, username_layout)

        self.login_button = QPushButton('Login')
        form_layout.addRow(self.login_button)

        layout.addLayout(form_layout)
        self.setLayout(layout)

        self.username_edit.returnPressed.connect(self.on_line_edit_user_name_pressed)
        self.login_button.clicked.connect(self.on_line_edit_user_name_pressed)

    @pyqtSlot()
    def on_line_edit_user_name_pressed(self):
        name = self.username_edit.text()
        self.username_edit.setText('')
        self._model.set_username(name)