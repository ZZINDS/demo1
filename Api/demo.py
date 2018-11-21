# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/8 14:30
@Author  : ZZINDS
@Site    : 
@File    : demo
@Software: PyCharm
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/a')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run('0.0.0.0', 80,)