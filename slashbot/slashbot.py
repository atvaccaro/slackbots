from flask import Flask, jsonify, request
import chungisms, morse_script, hashlib, duck

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/morse', methods=['GET', 'POST'])
def morse():
    if request.method == 'POST':
        if request.form['text']:
            chars = list(request.form['text'])
            if any([not c.isalnum() for c in chars]):
                return 'Unacceptable input, my dear friend.'
            return jsonify(response_type = 'in_channel', text = morse_script.encode_morse(request.form['text']))
        else:
            return "You need to add text to convert"
    else:
        return "You need to add text to convert"

@app.route('/demorse', methods=['GET', 'POST'])
def demorse():
    if request.method == 'POST':
        if request.form['text']:
            chars = list(request.form['text'])
            if any([c not in '-. ' for c in chars]):
                return 'Unacceptable input, my dear friend.'
            return jsonify(response_type = 'in_channel', text = morse_script.decode_morse(request.form['text']))
        else:
            return "You need to add text to convert"
    else:
        return "You need to add text to convert"


@app.route('/chungism', methods=['GET', 'POST'])
def chungism():
    if request.method == 'GET':
        return jsonify(response_type = 'in_channel', text = chungisms.get_wisdom())
    else:
        return 'You shall not POST'

@app.route('/md5', methods=['GET', 'POST'])
def md5():
    if request.method == 'POST':
        if request.form['text']:
            return jsonify(response_type='in_channel', text=hashlib.md5(request.form['text']).hexdigest())
        else:
            return 'You need to add text to hash'
    else:
        return 'You shall not GET!'


@app.route('/duck', methods=['POST'])
def duck():
    if request.form['text']:
        return jsonify(response_type='in_channel', text=duck.get(request.form['text']))
    else:
        return 'You need to add text to search for'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
