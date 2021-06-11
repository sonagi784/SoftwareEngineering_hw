from flask_login import UserMixin
from diary import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    # 가상 필드 author를 만들어줌, posts 사용자에게 속성 추가
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    # print(class)
    def __repr__(self):
        return '<User {}, {}, {}, {}>'.format(self.id, self.username, self.email, self.password_hash)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def followed_posts(self):
        own = Post.query.filter_by(user_id=self.id)
        return own.order_by(Post.timestamp.desc()) 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # print(class)
    def __repr__(self):
        return '<Post {}, {}, {}, {}, {}>'.format(self.id, self.title, self.body, self.timestamp, self.user_id)


# session에서 user_id에 맞는 객체를 리로드함
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

