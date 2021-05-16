from pybo import db

class Question(db.Model):#질문 DB
    id = db.Column(db.Integer, primary_key=True)#질문 데이터의 고유 번호
    subject = db.Column(db.String(200), nullable=False)#질문 제목
    content = db.Column(db.Text(), nullable=False)#질문 내용
    create_date = db.Column(db.DateTime(), nullable=False)#질문 작성일시
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))



class Answer(db.Model):#답변 DB
    id = db.Column(db.Integer, primary_key=True)#답변 데이터의 고유 번호
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))#질문 데이터의 고유 번호
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))#답변 내용
    content = db.Column(db.Text(), nullable=False)#답변 내용
    create_date = db.Column(db.DateTime(), nullable=False)#답변 작성일시
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))

class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)#중복 저장 방지
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)#중복 저장 방지

'''
class List(db.Model):
    id = db.Column(db.Integer)
    spelling = db.Column()
    meaning = db.Column()
'''