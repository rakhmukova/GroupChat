from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QSizePolicy

from Client.GUI.views.Chat.DisplayMessageWidget import DisplayMessageWidget


class DisplayMessagesArea(QScrollArea):
    def __init__(self):
        super(DisplayMessagesArea, self).__init__()

        self.setObjectName('messagesArea')
        self.setWidgetResizable(True)

        scroll_content = QWidget(self)
        scroll_content.setObjectName('messages')
        self.setWidget(scroll_content)

        self._scroll_layout = QVBoxLayout(scroll_content)
        self._scroll_layout.addStretch(10)
        self._scroll_layout.setObjectName('messagesLayout')
        scroll_content.setLayout(self._scroll_layout)

    def scroll_down(self):
        vbar = self.verticalScrollBar()
        vbar.setValue(vbar.maximum())

    def update_chat(self, sender, content):
        if sender is None or content is None:
            return

        message_card = DisplayMessageWidget(sender, content)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        message_card.setSizePolicy(size_policy)
        self._scroll_layout.addWidget(message_card, stretch=1)
        self.scroll_down()

    def clear_messages(self):
        for i in range(self._scroll_layout.count()):
            widget = self._scroll_layout.itemAt(i).widget()
            # widget.setParent(None)
            widget.deleteLater()
