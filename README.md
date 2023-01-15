# GroupChat

## About
This is a simple Python group chat application developed using [sockets](https://docs.python.org/3/library/socket.html) and [PyQt6](https://pypi.org/project/PyQt6/).

<img alt="image" src="https://user-images.githubusercontent.com/69808568/212559116-67090fd9-6f9f-4315-9299-a1dc6bac2e38.png">

## Installation

1. Clone the repository:

```commandline
git clone https://github.com/rakhmukova/GroupChat.git
```

2. Install the required packages:

```commandline
pip install -r requirements.txt
```

3. Create a .env file in the root directory of the project 
with the following format:

```
SERVER_PORT=<port>
SERVER_HOST=<address>
```

## Usage

1. Start the server:

```commandline
python server/main.py
```

To start the console version of the client, run:

```
python client/console/main.py <client_port>
```

To start the GUI version of the client, run:

```
python client/gui/main.py <client_port>
```
