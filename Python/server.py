from flask import Flask, request
server = Flask(__name__)
db = open("cards.txt", "r")
print(db.readline(1))
@server.route('/')
def hello():
    return "Hello World!"

@server.route('/read')
def read():
    
    card = request.args.get('card')
    print("ID карты:", card)
    #Эта проверка работает. Проблема была в типе данных
    if card in cards:
        return "Проходите"
    else:
        return "Прохода нет"


if __name__ == '__main__':
    #192.168.1.153
    server.run(host='192.168.1.153', port=4567)

db.close()