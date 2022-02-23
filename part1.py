from flask import Flask
import requests
import json


def chuck():
    x = r"http://api.icndb.com/jokes/random/10"
    data = requests.get(x)
    jokes = json.loads(data.text)
    temp = ''
    for i in jokes["value"]:
        temp = temp + (i["joke"] + '<br>')
    return temp


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>To view 10 random chuck norris jokes <a href=http://127.0.0.1:5000/getJokes> click here</a></h1>'


@app.route('/getJokes')
def form_example():
    return chuck()


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    # if the below mentioned port is not available, please use a diffrent port
    app.run(port=5000, debug=True)
