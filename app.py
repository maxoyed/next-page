from flask import Flask, render_template, request
from pynput.keyboard import Key, Controller
from socket import gethostname, gethostbyname
from qrcode_terminal import draw

app = Flask(__name__)
keyboard = Controller()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/page')
def page():
    direction = request.args.get('direction')
    keyboard.press(Key[direction])
    keyboard.release(Key[direction])
    return {"message": direction}


if __name__ == '__main__':
    port = 5001
    hostname = gethostname()
    ip = gethostbyname(hostname)
    draw(f'http://{ip}:{port}')
    app.run(host='0.0.0.0', port=port, debug=False)
