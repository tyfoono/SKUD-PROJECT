from flask import Flask, jsonify, request
server = Flask(__name__)

name = "John"

@server.route('/')
def hello():
    return "Hello World!"


@server.route('/h')
def h():
    name = request.args.get('name')
    return "Hello " + name + "!"


if __name__ == '__main__':
    server.run(host='192.168.1.153', port=4567)
