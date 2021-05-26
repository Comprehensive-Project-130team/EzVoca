from flask import Blueprint, url_for, render_template, flash, request, session, g
import random
from pybo import db
from pybo.models import User, Voca, VocaWord
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/hello')
def hello_pybo():
    return 'EZVoca!'


@bp.route('/')
def index():
    return redirect(url_for('auth.index'))

@bp.route('/dash/')
def dash():
    voca_list = Voca.query.filter_by(user=g.user).all()
    return render_template("dashboard.html",voca_list=voca_list)

@bp.route('/voca/')
def voca():
    voca_list = Voca.query.filter_by(user=g.user).all()
    voca_map = {}
    for voca in voca_list:
        voca_map[voca] = VocaWord.query.filter_by(voca=voca).all()
    return render_template("voca.html", voca_list=voca_list, voca_map=voca_map)

@bp.route('/voca_detail/<vocaid>')
def voca_detail(vocaid):
    voca = Voca.query.filter_by(id=vocaid).first()
    voca_list = VocaWord.query.filter_by(voca=voca).all()
    return render_template("voca_detail.html", voca=voca, voca_list=voca_list)

@bp.route('/account/')
def account():
    return render_template("account.html")

@bp.route('/vocacreate/test', methods=["POST","GET"])
def create_test():
    out = "<h1>VocaSets</h1>\n<pre>"
    for vs in Voca.query.filter_by(user=g.user).all():
        out += f"\n{vs.vocaname}, id={vs.id}, tag={vs.tag}, user={vs.user_id}"
        for v in VocaWord.query.filter_by(voca=vs).all():
            out += f"\n  -  {v.word} : {v.mean}"
    out += "<hr/>"
    return out

@bp.route('/voca/<vocaid>/edit', methods=["POST", "GET"])
def voca_edit(vocaid):
    vocaset = Voca.query.filter_by(id=vocaid).first()
    voca_list = VocaWord.query.filter_by(voca=vocaset).all()

    if request.method == 'POST':
        words = request.form.getlist('word[]')
        means = request.form.getlist('mean[]')

        vocaset.user = g.user
        vocaset.tag = request.form['tag']
        vocaset.vocaname = request.form['title']

        for v in voca_list:
            db.session.delete(v)
        db.session.commit()
        for v in filter(lambda w:w[0], zip(words, means)):
            voca = VocaWord(voca=vocaset, word=v[0], mean=v[1])
            db.session.add(voca)
        db.session.commit()
        return redirect(url_for('main.dash'))
    return render_template("voca_create.html", voca=vocaset, voca_list=voca_list)

@bp.route('/vocacreate', methods=["POST", "GET"])
def create():
    if request.method == 'POST':
        words = request.form.getlist('word[]')
        means = request.form.getlist('mean[]')
        vocaset = Voca(vocaname=request.form['title'], user=g.user, tag=request.form['tag'])
        db.session.add(vocaset)
        for v in filter(lambda w:w[0], zip(words, means)):
            voca = VocaWord(voca=vocaset, word=v[0], mean=v[1])
            db.session.add(voca)
        db.session.commit()
        return redirect(url_for('main.voca'))
    return render_template("voca_create.html")

@bp.route('/word/<voca_id>', methods=["GET"])
def word(voca_id):
    try:
        count = int(request.args.get('count', 1))
    except:
        count = 1
    if voca_id == None:
        return redirect(url_for('main.voca'))
    voca_set = VocaWord.query.filter_by(voca_id=voca_id).all()

    return render_template("word.html", voca_id=voca_id, count=count, voca_set=voca_set)

@bp.route('/voca/<voca_id>/delete', methods=["GET"])
def word_delete(voca_id):
    voca = Voca.query.filter_by(id=voca_id).first()
    db.session.delete(voca)
    db.session.commit()
    return redirect(url_for('main.voca'))



@bp.route('/word_test_result', methods=["GET"])
def word_test_result():
    data = session['message']
    voca_set = Voca.query.filter_by(id=data['voca_id']).first()
    print(voca_set)
    # del session['message']
    return render_template("word_test_result.html", voca_set=voca_set,
                           correct=data["correct"], total=data["total"])

@bp.route('/word_test/<voca_id>', methods=["GET"])
def word_test(voca_id):
    selects = request.args.get('select') or ''
    count = len(selects) + 1

    if not selects: # 첫문제인 경우 seed 를 새로 생성한다.
        session['seed'] = random.randint(0, 99)
        print(f'new seed: {session["seed"]}')
    random.seed(session['seed']) # 항상 같은 랜덤값이 나오도록 한다.
    # voca = Voca.query.filter_by(id=voca_id).first()
    voca_list = VocaWord.query.filter_by(voca_id=voca_id).all()
    total = len(voca_list)

    answers = [random.randint(1,4) for _ in range(total)]
    print(f'seed: {session["seed"]}, select={selects}, answer={answers}')

    if total==0:
        return render_template("word_test.html",voca_id=voca_id, voca=None, select=None,
                           count=None, total=None, options=None)
    if total>0 and total < count:
        correct = sum(map(lambda v: v[0] == str(v[1]), zip(selects, answers)))
        session['message'] = {
            "voca_id" : voca_id,
            "correct": correct,
            "total": total
        }
        return redirect(url_for('main.word_test_result'))

    random.shuffle(voca_list)
    voca = voca_list[count-1] # 현재 단어
    voca_list.remove(voca)
    random.shuffle(voca_list)
    options = list(map(lambda v:v.mean, voca_list))
    if len(options) < 3: # 보기 수가 3개 이하인 경우 임의의 단어를 넣는다.
        options += ["사과", "다리", "시험", "다음"]
        options = options[:3] # 다시 보기를 3개로 자른다.

    answer = answers[count - 1] - 1
    options.insert(answer, voca.mean) # 정답 위치에 정답을 넣는다.

    return render_template("word_test.html",
                           voca_id=voca_id, voca=voca, select=selects,
                           count=count, total=total, options=options)
