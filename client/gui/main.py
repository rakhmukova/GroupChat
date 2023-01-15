import sys

from client.gui.views.app import App

if __name__ == '__main__':
    app = App(sys.argv)
    app.exec()
