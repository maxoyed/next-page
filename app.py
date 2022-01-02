from flask import Flask, render_template, request
from pynput.keyboard import Key, Controller
import socket
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


def draw_url_qrcode(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    draw(f'http://{ip}:{port}')
    s.close()


if __name__ == '__main__':
    port = 5001
    draw_url_qrcode(port)
    app.run(host='0.0.0.0', port=port, debug=False)
