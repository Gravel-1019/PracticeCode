# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # 获取前端传递过来的用户名和密码
    username = request.form['username']
    password = request.form['password']

    # 假设用户名为admin，密码为password
    if username == 'admin' and password == 'password':
        # 登录成功，重定向到欢迎页面
        return redirect(url_for('welcome'))
    else:
        # 登录失败，重定向到登录页面
        return redirect(url_for('index'))

@app.route('/welcome')
def welcome():
    return "Welcome!"

if __name__ == '__main__':
    app.run(debug=True)