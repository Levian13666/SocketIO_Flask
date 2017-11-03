from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def route():
    return app.send_static_file('index.html')


@socketio.on('my_event', namespace='/connection')
def test_message(message):
    print(message['data'])
    emit('connected', {'data': 'Successfully connected!'})

socketio.run(app, port=8080)
