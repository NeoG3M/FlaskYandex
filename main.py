from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер', 'строитель', "врач", "водитель", "биолог", "геодезист"]
    return render_template('list_prof.html', list=list, profs=profs)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    answ_dict = {"title": "Анкета",
                 "surname": "Сева",
                 "name": "Иван",
                 "education": "Среднее общее",
                 "profession": "Геодезист",
                 "sex": "Мужской",
                 "motivation": "Меня папа позвал",
                 "ready": True}
    return render_template('auto_answer.html', **answ_dict)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
