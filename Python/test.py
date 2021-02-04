from flask import Flask, request
server = Flask(__name__)

@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def read():
    cards = ["138e25d8", "337c28d8", "3", "2"]
    card = request.args.get('card')
    print("ID карты:", card)
    #Эта проверка работает. Проблема была в типе данных
    if card in cards:
        return "Проходите"
    else:
        return "Прохода нет"


if __name__ == '__main__':
    #192.168.1.153
    server.run(host='192.168.0.75', port=4567)