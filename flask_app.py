from flask import Flask, render_template
from pynput.keyboard import Key, Controller
from socket import gethostname, gethostbyname
from qrcode_terminal import draw

app = Flask(__name__)
keyboard = Controller()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/next-page')
def next_page():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    return render_template('index.html')


if __name__ == '__main__':
    port = 5001
    hostname = gethostname()
    ip = gethostbyname(hostname)
    draw(f'http://{ip}:{port}')
    app.run(host='0.0.0.0', port=port, debug=False)
