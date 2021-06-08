from flask import render_template, flash, redirect, request
from flask.helpers import url_for
from flask_login import current_user, login_user, logout_user, login_required
from diary import app, db
from diary.models import User, Post
from diary.forms import LoginForm, RegistrationForm, PostForm
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    # Post form이 제출된 경우
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post have been uploaded!')
        return redirect(url_for('index'))
    
    # 아직 Post form이 제출되지 않은 경우 / Post list
    posts = current_user.followed_posts().all()
    return render_template("index.html", title='Home Page', form=form, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 인증(로그인 확인)된경우
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    # 로그인 form이 제출된 경우
    if form.validate_on_submit():
        # form에 제출된 양식에 맞는 User instance를 db에 검색함
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # Login and validate the user. user should be an instance of your `User` class
        login_user(user, remember=form.remember_me.data)
        # next_page = login_required에 막혀 못가던 page
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('index'))
        return redirect(next_page)
    # 아직 로그인 form이 제출되지 않은 경우 (처음엔 여길 지나감)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 로그인되어있는 경우 index로 리다이렉트 시킴
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    # 회원가입 form이 제출된 경우
    if form.validate_on_submit():
        # form에 맞춰 User instance를 만들고 db에 추가
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    # 아직 회원가입 form이 제출되지 않은 경우 (처음엔 여길 지나감)
    return render_template('register.html', title='Register', form=form)


@app.route('/explore')
@login_required
def explore():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title='Explore', posts=posts)