from flask import Flask, jsonify, request
server = Flask(__name__)

cards = [10, 1, 3, 2]

@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def h():
    card = request.args.get('card')
    print(card)
    return card

if __name__ == '__main__':
    #192.168.1.153
    server.run(host='192.168.0.75', port=4567)