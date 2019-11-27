from flask import Flask
from config import DEBUG

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/linzero/')
def hello_linzero():
    return 'Hello linzero!'


@app.route('/w/')
def hello_w():
    return 'Hello w!'


@app.route('/h/')
def hello_h():
    return 'Hello h!'


# app.add_url_rule('/hello', view_func=hello_w)

if __name__ == '__main__':
    print('app:', app.url_map)
    app.run(host='0.0.0.0', port=5008, debug=DEBUG)
