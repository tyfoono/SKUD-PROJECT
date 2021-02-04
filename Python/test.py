from flask import Flask, request
server = Flask(__name__)



@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def read():
    cards = [10, 1, 3, 2]
    card = request.args.get('card')
    print("ID карты:", card)
    #эта проверка не работает
    if card in cards:
        return "Проходите"
    else:
        return "Прохода нет"
    '''
    Проблема именно в проверке.
    ID карты считывается правильно.
    Либо не код не видит список, либо я проблема в коде 
    '''

if __name__ == '__main__':
    #192.168.1.153
    server.run(host='192.168.0.75', port=4567)