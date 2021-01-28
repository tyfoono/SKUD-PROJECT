from flask import Flask
server = Flask(__name__)



@server.route('/')
def hello():
    return "Hello World!"


@server.route('/david')
def david():
    return "Hello David!"


if __name__ == '__main__':
    server.run(host='192.168.1.153', port=4567)
