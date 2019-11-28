from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')
print('DEBUG:', app.config['DEBUG'])


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
      q:普通关键字 isbn
      page:
      count:
      isbn: isbn13 13个0到9的数字组成
      isbn10 10个0-9的数字组成 ，含一些特殊符号‘-‘
    """
    isbn_or_key = is_isbn_or_key(q)
    return isbn_or_key


@app.route('/linzero/')
def hello_linzero():
    return 'Hello linzero!'


@app.route('/w/')
def hello_w():
    return 'Hello w!'


@app.route('/h/')
def hello_h():
    return '<html><html>'


# app.add_url_rule('/hello', view_func=hello_w)

if __name__ == '__main__':
    print('app:', app.url_map)
    app.run(host='0.0.0.0', port=5008, debug=app.config['DEBUG'])
