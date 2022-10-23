from flask import Flask
from flask import request
from markupsafe import escape

import face_recognition
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/auth/login', method='POST')
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            return 'Invalid username/password'
    return 'Invalid request'

# @app.route('/auth/logout', method='POST')
# def logout():
#     if request.method == 'POST':
#         return 'Logout'

@app.route('/auth/signup', method='POST')
def signup():
    if request.method == 'POST':
        if valid_signup(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            return 'Invalid username/password'
    return 'Signup'

# マイページの表示情報、更新
@app.route('/mypage', methods=['GET', 'POST'])
def mypage():
    if request.method == 'POST':
        if request.files.length:
            f = request.files[0]
            f.save('/var/www/uploads/uploaded_file.txt')
    return 'This is my page!'

# 他ユーザーの表示情報
@app.route('/user/<username>', method='GET')
def show_user_profile(username):
    # show the user profile for that user
    return f'{escape(username)}\'s page!'

@app.route('/search', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if request.files.length:
            f = request.files[0]
            # GPUがないため、cnnではなくhogを使用
            loc = face_recognition.face_locations(img, model="hog")
            assert len(loc) >= 1, "顔の検出に失敗"
            assert len(loc) <= 1, "複数の顔を検出"
            face_img_to_check = face_recognition.load_image_file(f)
