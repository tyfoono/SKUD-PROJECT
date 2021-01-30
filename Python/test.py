from flask import Flask, jsonify, request
server = Flask(__name__)

name = "John"

@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def h():
    card = request.args.get('card')
    print(card)
    return "Hello " + card + "!"

if __name__ == '__main__':
    server.run(host='192.168.1.153', port=4567)