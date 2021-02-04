from flask import Flask, request
server = Flask(__name__)

@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def read():
    cards = ["10", "1", "3", "2"]
    card = request.args.get('card')
    print("ID карты:", card)
    #Эта проверка не работает. Всегда выдаёт "Прохода нет"
    if card in cards:
        return "Проходите"
    else:
        return "Прохода нет"
    """
    Проблема именно в проверке.
    ID карты считывается правильно.
    Видимо, код не видит список 
    """

if __name__ == '__main__':
    #192.168.1.153
    server.run(host='192.168.0.75', port=4567)