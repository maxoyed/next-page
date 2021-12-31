from flask import Flask, render_template
from pynput.keyboard import Key, Controller

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
    app.run(host='0.0.0.0', debug=True)
