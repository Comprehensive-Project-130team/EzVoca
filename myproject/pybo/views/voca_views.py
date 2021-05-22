from flask import Blueprint, url_for, render_template, request, session, g
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import VocaCreateForm
from pybo.models import Vocabulary, Vocabulary_word
import functools

bp = Blueprint('voca', __name__, url_prefix='/voca')


@bp.route('/create/', methods=('GET', 'POST'))
def create_voca():
    form = VocaCreateForm()
    print("get!")
    if request.method == 'POST' and form.validate_on_submit():
        print("post!")
        vocabulary = Vocabulary(user_id=g.user.id, voca_name=form.voca_name.data, voca_tag=form.voca_tag.data)
        db.session.add(vocabulary)
        db.session.commit()
        voca_word = Vocabulary_word(voca_id=vocabulary.voca_id, voca_word=form.word1.data, voca_word_mean=form.mean1.data)
        voca_word2 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word2.data, voca_word_mean=form.mean2.data)
        voca_word3 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word3.data, voca_word_mean=form.mean3.data)
        voca_word4 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word4.data, voca_word_mean=form.mean4.data)
        voca_word5 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word5.data, voca_word_mean=form.mean5.data)
        voca_word6 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word6.data, voca_word_mean=form.mean6.data)
        voca_word7 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word7.data, voca_word_mean=form.mean7.data)
        voca_word8 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word8.data, voca_word_mean=form.mean8.data)
        voca_word9 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word9.data, voca_word_mean=form.mean9.data)
        voca_word10 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word10.data, voca_word_mean=form.mean10.data)
        voca_word11 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word11.data, voca_word_mean=form.mean11.data)
        voca_word12 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word12.data, voca_word_mean=form.mean12.data)
        voca_word13 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word13.data, voca_word_mean=form.mean13.data)
        voca_word14 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word14.data, voca_word_mean=form.mean14.data)
        voca_word15 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word15.data, voca_word_mean=form.mean15.data)
        voca_word16 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word16.data, voca_word_mean=form.mean16.data)
        voca_word17 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word17.data, voca_word_mean=form.mean17.data)
        voca_word18 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word18.data, voca_word_mean=form.mean18.data)
        voca_word19 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word19.data, voca_word_mean=form.mean19.data)
        voca_word20 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word20.data, voca_word_mean=form.mean20.data)
        voca_word21 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word21.data, voca_word_mean=form.mean21.data)
        voca_word22 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word22.data, voca_word_mean=form.mean22.data)
        voca_word23 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word23.data, voca_word_mean=form.mean23.data)
        voca_word24 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word24.data, voca_word_mean=form.mean24.data)
        voca_word25 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word25.data, voca_word_mean=form.mean25.data)
        voca_word26 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word26.data, voca_word_mean=form.mean26.data)
        voca_word27 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word27.data, voca_word_mean=form.mean27.data)
        voca_word28 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word28.data, voca_word_mean=form.mean28.data)
        voca_word29 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word29.data, voca_word_mean=form.mean29.data)
        voca_word30 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word30.data, voca_word_mean=form.mean30.data)
        voca_word31 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word31.data, voca_word_mean=form.mean31.data)
        voca_word32 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word32.data, voca_word_mean=form.mean32.data)
        voca_word33 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word33.data, voca_word_mean=form.mean33.data)
        voca_word34 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word34.data, voca_word_mean=form.mean34.data)
        voca_word35 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word35.data, voca_word_mean=form.mean35.data)
        voca_word36 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word36.data, voca_word_mean=form.mean36.data)
        voca_word37 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word37.data, voca_word_mean=form.mean37.data)
        voca_word38 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word38.data, voca_word_mean=form.mean38.data)
        voca_word39 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word39.data, voca_word_mean=form.mean39.data)
        voca_word40 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word40.data, voca_word_mean=form.mean40.data)
        voca_word41 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word41.data, voca_word_mean=form.mean41.data)
        voca_word42 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word42.data, voca_word_mean=form.mean42.data)
        voca_word43 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word43.data, voca_word_mean=form.mean43.data)
        voca_word44 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word44.data, voca_word_mean=form.mean44.data)
        voca_word45 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word45.data, voca_word_mean=form.mean45.data)
        voca_word46 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word46.data, voca_word_mean=form.mean46.data)
        voca_word47 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word47.data, voca_word_mean=form.mean47.data)
        voca_word48 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word48.data, voca_word_mean=form.mean48.data)
        voca_word49 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word49.data, voca_word_mean=form.mean49.data)
        voca_word50 = Vocabulary_word(voca_id=voca_word.voca_id, voca_word=form.word50.data, voca_word_mean=form.mean50.data)

        voca_list=[voca_word, voca_word2, voca_word3, voca_word4, voca_word5, voca_word6, voca_word7, voca_word8, voca_word9, voca_word10,
                   voca_word11, voca_word12, voca_word13, voca_word14, voca_word15, voca_word16, voca_word17, voca_word18, voca_word19, voca_word20,
                   voca_word21, voca_word22, voca_word23, voca_word24, voca_word25, voca_word26, voca_word27, voca_word28, voca_word29, voca_word30,
                   voca_word31, voca_word32, voca_word33, voca_word34, voca_word35, voca_word36, voca_word37, voca_word38, voca_word39, voca_word40,
                   voca_word41, voca_word42, voca_word43, voca_word44, voca_word45, voca_word46, voca_word47, voca_word48, voca_word49, voca_word50]
        for voca in voca_list:
            if voca.voca_word != '':
                db.session.add(voca)
        db.session.commit()
        return redirect(url_for('main.dash'))
    return render_template("voca_create.html", form=form)

@bp.route('/', methods=('GET', 'POST'))
def view_voca():
    voca_db=Vocabulary.query.all()
    voca_list = []
    for voca in voca_db:
        if voca.user_id == g.user.id:
            voca_list.append(voca)
    word_list=Vocabulary_word.query.all()
    dic = {1: 0}

    for i in range(len(word_list)):
        if word_list[i].voca_id in dic:
            dic[word_list[i].voca_id] += 1
        else:
            dic[word_list[i].voca_id] = 1
    return render_template("voca.html", voca_list=voca_list, num=dic)

@bp.route('/detail/<int:voca_id>/')
def detail(voca_id):
    word_list = Vocabulary_word.query.filter_by(voca_id=voca_id).all()


    return render_template("voca_detail.html", word_list=word_list)
