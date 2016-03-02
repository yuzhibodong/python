#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-02-28 17:53:14
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html",
                           title='Sign In',
                           form=form)
