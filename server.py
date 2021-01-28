from flask import Flask, jsonify, request
server = Flask(__name__)

cards = []

@server.route('/')
def hello():
    return "Hello World!"


@server.route('/david')
def david():
    return "Hello David!"

@server.route('/check')
def check():
    answer = dict()
    cardID = request.args.get('cardID')
    if cardID in cards:
        answer['status'] = 200
        answer['message'] = "Проходите"
    return jsonify(answer)

if __name__ == '__main__':
    server.run(host='192.168.1.153', port=4567)
