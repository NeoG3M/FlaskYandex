from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/index')
def promotion():
    lines = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнем с Марса!',
             'Присоединяйся!']
    return '<br>'.join(lines)


@app.route('/image_mars')
def mars():
    url_image = url_for('static', filename='img/mars.png')
    return f'''<h2>Жди нас, Марс!</h2>
            <img src="{url_image}" alt="There had to be mars image">
            <h3>Вот она какая, красная планета...</h3>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
