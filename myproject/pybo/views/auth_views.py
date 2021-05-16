from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm, UserPWchangeForm
from pybo.models import User
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.index'))
        return view(**kwargs)
    return wrapped_view


@bp.route('/register/', methods=('GET', 'POST'))
def register():#회원가입
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),#입력받은 비밀번호를 암호화하여 저장
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.index'))
        else:
            flash('이미 존재하는 아이디 입니다.')
    return render_template('register.html', form=form)
@bp.route('/index/', methods=('GET', 'POST'))
def index():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.dash'))
        flash(error)
    return render_template('/index.html', form=form)
# --------------------------------- [05.16 고진석 비밀번호 변경 기능] ---------------------------------- #
@bp.route('/changepw/', methods=('GET', 'POST'))
def changepw():
   form = UserPWchangeForm()
   if request.method == 'POST' and form.validate_on_submit():
       error = None
       g.user.password = generate_password_hash(form.password1.data)#로그인이 된 사용자의 새 비밀번호와 비밀번호 확인을 비교함
       db.session.commit()#DB에 저장
       return redirect(url_for('main.dash'))#회원가입이 완료되면 대시보드로 이동
       #print(g.user.password)

   return render_template('/changepw.html', form=form)
# --------------------------------- [edit] ---------------------------------- #
@bp.route('/account/', methods=('GET', 'POST'))
def account():
    if request.method == 'POST':
       error = None
       db.session.delete(g.user)
       db.session.commit()
       return redirect(url_for('auth.index'))
    return render_template('/account.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))