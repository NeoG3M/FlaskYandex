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


@app.route('/promotion_image')
def mars_promotion():
    url_css = url_for('static', filename='css/style.css')
    url_image = url_for('static', filename='img/mars.png')
    lines = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнем с Марса!',
             'Присоединяйся!']
    return '''<!doctype html>
                <html lang="ru">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport"
                          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                    <link rel="stylesheet" type="text/css" href="{}">
                    <title>Document</title>
                </head>
                <body>
                <h1>Жди нас, Марс!</h2>
                <img src="{}" alt="There had to be mars image">
                <div class="alert alert-primary" role="alert">
                    {}
                </div>
                <div class="alert alert-secondary" role="alert">
                  {}
                </div>
                <div class="alert alert-success" role="alert">
                {}
                </div>
                <div class="alert alert-danger" role="alert">
                {}
                </div>
                <div class="alert alert-warning" role="alert">
                {}
                </div>
                </body>
                </html>
        '''.format(url_css, url_image, *lines)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
