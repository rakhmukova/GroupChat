import sys

from Client.GUI.views.app import App

if __name__ == '__main__':
    app = App(sys.argv)
    app.exec()
