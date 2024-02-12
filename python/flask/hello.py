# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()