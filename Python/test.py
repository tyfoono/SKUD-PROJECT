from flask import Flask, jsonify, request
server = Flask(__name__)

cards = []

@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def h():
    card = request.args.get('card')
    print(card)
    if card in cards:
        answer = "Проходите"
    else:
        answer = "Прохода нет"
    return answer
    
if __name__ == '__main__':
    #192.168.1.153
    server.run(host='192.168.0.75', port=4567)