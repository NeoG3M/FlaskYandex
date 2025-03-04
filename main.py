from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/promotion')
def promotion():
    lines = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнем с Марса!',
             'Присоединяйся!']
    return '<br>'.join(lines)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
