from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index():
    """
    Создание главной страницы
    """
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    """
    Создание представления для вывода данных про кандидата
    """
    candidate = utils.get_candidate_by_pk(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    """
    Создание представления поиска по имени
    """
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skills(skill):
    """
    Создание представления поиска по навыку
    """
    candidates = utils.get_candidates_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))


app.run(debug=True)
