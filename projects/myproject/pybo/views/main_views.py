from flask import Blueprint, url_for, Flask, app, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('auth.index'))

@bp.route('/dash/')
def dash():
    return render_template("dashboard.html")


@bp.route('/voca/')
def voca():
    return render_template("voca.html")


@bp.route('/account/')
def account():
    return render_template("account.html")
