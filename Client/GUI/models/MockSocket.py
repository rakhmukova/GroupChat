import json
import time
from datetime import datetime

from essential_generators import DocumentGenerator
import names


class MockSocket:
    def __init__(self):
        self.message_num = 0
        self.sentence_generator = DocumentGenerator()

    def bind(self, __address):
        pass

    def connect(self, __address):
        pass

    def setsockopt(self,  __level, __optname, __value):
        pass

    def recv(self, __bufsize):
        time.sleep(2)
        x = {
            'sender_name': f'{names.get_first_name()}',
            'content': f'{self.sentence_generator.sentence()}',
            'sending_time': datetime.now().strftime('%H:%M:%S'),
        }
        self.message_num += 1
        return bytes(json.dumps(x), 'utf-8')

    def send(self, data):
        pass
