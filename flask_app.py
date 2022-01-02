from flask import Flask, render_template
from pynput.keyboard import Key, Controller
from socket import gethostname, gethostbyname
from qrcode_terminal import draw

app = Flask(__name__)
keyboard = Controller()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/left')
def left():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    return {"message": "left"}


@app.route('/right')
def right():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    return {"message": "right"}


if __name__ == '__main__':
    port = 5001
    hostname = gethostname()
    ip = gethostbyname(hostname)
    draw(f'http://{ip}:{port}')
    app.run(host='0.0.0.0', port=port, debug=False)
