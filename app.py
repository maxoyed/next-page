from flask import Flask, request, render_template_string
from pynput.keyboard import Key, Controller
import socket
from qrcode_terminal import draw

app = Flask(__name__)
keyboard = Controller()


@app.route("/")
def index():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>小说翻页</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      border: 0;
    }

    .container {
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
    }

    button {
      width: 100%;
      height: 50vh;
      background-color: #000;
      color: #fff;
      font-size: 1.5em;
      box-sizing: border-box;
      outline: none;
    }

    #left {
      border-bottom: 1px solid #fff;
    }
  </style>
</head>

<body>
  <div class="container">
    <button id="left">上一页</button>
    <button id="right">下一页</button>
  </div>
  <script>
    const left = document.getElementById("left");
    const right = document.getElementById("right");
    const page = (direction) => {
      const httpRequest = new XMLHttpRequest();
      httpRequest.open('GET', `/page?direction=${direction}`, true);
      httpRequest.send();
      httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
          const json = httpRequest.responseText;
          console.log(JSON.parse(json));
        }
      };
    };
    left.onclick = () => {
      page("left");
    };
    right.onclick = () => {
      page("right");
    };
  </script>
</body>

</html>
""")


@app.route("/page")
def page():
    direction = request.args.get("direction")
    keyboard.press(Key[direction])
    keyboard.release(Key[direction])
    return {"message": direction}


def draw_url_qrcode(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    draw(f"http://{ip}:{port}")
    s.close()


if __name__ == "__main__":
    port = 5001
    draw_url_qrcode(port)
    app.run(host="0.0.0.0", port=port, debug=False)
