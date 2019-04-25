from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from schoolsystem import app, login_manager
from flask_migrate import Migrate
from flask_login import UserMixin,current_user
from datetime import date
from flask import current_app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(180))
    name = db.Column(db.String(30))
    role = db.Column(db.String(30))
    xy = db.Column(db.String(50))
    articles = db.relationship('Note_yet', lazy='dynamic')
    articles_Note = db.relationship('Note')

    @staticmethod
    def query_all(name, stime, etime, matter,page=1):
        activites = current_user.articles
        if name != '':
            activites = activites.filter(Note_yet.xm.like('%' + name + '%'))
        if stime != '' and etime == '':
            # etime = stime
            activites = activites.filter(Note_yet.created_date == stime)
        elif stime != '' and etime != '':
            activites = activites.filter(Note_yet.created_date.between(stime, etime))
        else:
            pass
        if matter != 'info':
            activites = activites.filter(Note_yet.zt == matter)
        return activites.paginate(
            page, per_page=current_app.config['POST_PER_PAGE']
        )


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xh = db.Column(db.String(128))
    xm = db.Column(db.String(10))
    xy = db.Column(db.String(50))
    bj = db.Column(db.String(30))
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))
    status = db.Column(db.String(10))


# 学生输入姓名账号后，从Note中复制得到的表
class Note_yet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xh = db.Column(db.String(128))
    xm = db.Column(db.String(10))
    xy = db.Column(db.String(50))
    bj = db.Column(db.String(30))
    zt = db.Column(db.String(30))
    created_date = db.Column(db.Date, default=date.today)
    reason = db.Column(db.String(256))
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))
    status = db.Column(db.String(10))
    home_address = db.Column(db.String(50))         #家庭地址
    home_tel = db.Column(db.String(12))             #家庭通讯
    per_tel = db.Column(db.String(12))              #个人通讯
    identity = db.Column(db.String(18))             #身份证
    school_sttime = db.Column(db.String(16))        #入校时间
    school_endtime = db.Column(db.String(16))       #离校时间
    dom_campus = db.Column(db.String(10))           #校区
    dom_built = db.Column(db.String(5))             #宿舍楼号
    dom_dorm = db.Column(db.String(5))              #寝室号
    school = db.Column(db.String(50))               #学校
    campus = db.Column(db.String(20))               #院系
    code = db.Column(db.String(50))                 #证书编号
    sex = db.Column(db.String(5))                   #性别
    leng_school = db.Column(db.String(8))           #学制···未加
    discipline = db.Column(db.String(20))           #专业···未加




    @staticmethod  #静态回调
    def query_all(name, stime, etime, matter, department, page=1):
        activites = Note_yet.query
        if name != '':
            activites = activites.filter(Note_yet.xm.like('%' + name + '%'))
        if stime != '' and etime == '':
            # etime = stime
            activites = activites.filter(Note_yet.created_date == stime)
        elif stime != '' and etime != '':
            activites = activites.filter(Note_yet.created_date.between(stime, etime))
        else:
            pass
        if matter != 'info':
            activites = activites.filter(Note_yet.zt == matter)
        if department != 'admin':
            activites = activites.filter(Note_yet.xy == department)
        return activites.paginate(
            page, per_page=current_app.config['POST_PER_PAGE']
        )


# flask_login load_user函数
@login_manager.user_loader
def load_user(user_id):
    user = Admin.query.get(int(user_id))
    return user
