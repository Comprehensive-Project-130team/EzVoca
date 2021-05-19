from flask import Blueprint, url_for, Flask, app, render_template, g
from werkzeug.utils import redirect

from pybo.models import Vocabulary

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/hello')
def hello_pybo():
    return 'EZVoca!'


@bp.route('/')
def index():
    return redirect(url_for('auth.index'))

@bp.route('/dash/')
def dash():
    voca_db = Vocabulary.query.all()
    voca_list = []
    for voca in voca_db:
        if voca.user_id == g.user.id:
            voca_list.append(voca)

    return render_template("dashboard.html", voca_list=voca_list)

@bp.route('/account/')
def account():
    return render_template("account.html")


