from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Пример формы</title>
</head>
<body>
<h1>Анкета претендента</h1>
<h2>на участие в миссии</h2>
<div>
    <form class="login_form" method="post">
        <div class="form-block">
            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
        </div>

        <input type="email" class="form-control form-block" id="email" aria-describedby="emailHelp"
               placeholder="Введите адрес почты" name="email">
        <div class="form-group form-block">
            <label for="classSelect">Какое у Вас образование?</label>
            <select class="form-control" id="classSelect" name="eduClass">
                <option>Отсутствует</option>
                <option>Начальное</option>
                <option>Основное</option>
                <option>Среднее общее</option>
                <option>Среднее профессиональное</option>
                <option>Высшее: бакалавриат</option>
                <option>Высшее: специалитет</option>
                <option>Высшее: магистратура</option>
                <option>Высшее: аспирантура</option>
            </select>
        </div>
        <div class="form-block">
            <label for="educationBoxes">Какие у Вас есть образования?</label>
            <div id="educationBoxes">
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="engeneerExplorer" name="edu">
                    <label class="form-check-label" for="engeneerExplorer">Инженер-исследователь</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="engeneerBuilder" name="edu">
                    <label class="form-check-label" for="engeneerBuilder">Инженер-строитель</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="pilot" name="edu">
                    <label class="form-check-label" for="pilot">Пилот</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="meteorolgist" name="edu">
                    <label class="form-check-label" for="meteorolgist">Метеоролог</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="lifeEngeneer" name="edu">
                    <label class="form-check-label" for="lifeEngeneer">Инженер по жизнеобеспечению</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="radiationEngeneer" name="edu">
                    <label class="form-check-label" for="radiationEngeneer">Инженер по радиационной защите</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="doctor" name="edu">
                    <label class="form-check-label" for="doctor">Врач</label>
                </div>
            </div>
        </div>

        <div class="form-group form-block">
            <label for="form-check">Укажите пол</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                <label class="form-check-label" for="female">
                    Женский
                </label>
            </div>
        </div>

        <div class="form-group form-block">
            <label for="about">Почему Вы хотите принять участие в миссии?</label>
            <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
        </div>

        <div class="form-group form-block">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        
        <div class="form-group form-check form-block">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
        </div>
        <button type="submit" class="btn btn-primary">Готовы остаться на Марсе?</button>
    </form>
</div>
</body>
</html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['eduClass'])
        print(request.form['file'])
        print(request.form['motivation'])
        print(request.form['edu'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
