from flask import Flask

app = Flask(__name__)


@app.route('/linzero/')
def hello_world():
    return 'Hello linzero!'


# @app.route('/w/')
def hello_w():
    return 'Hello w!'


app.add_url_rule('/hello', view_func=hello_w)

if __name__ == '__main__':
    app.run(debug=True)
