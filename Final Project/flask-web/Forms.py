# -*- coding: utf-8 -*-
# @Time    : 2019/12/20
# @Author  : Liu Hanwen
# @File    : Forms.py

from __future__ import unicode_literals
from flask_wtf import FlaskForm

from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class EventListForm(FlaskForm):
    event = StringField('请输入学生参加的活动（老师您测试的时候随便输入都可以）', validators=[DataRequired(), Length(1, 64)])
    value = StringField('完成情况（老师您测试的时候随便输入都可以）', validators=[DataRequired(), Length(1, 64)])
    event_time = StringField('活动日期（老师您测试的时候随便输入都可以，建议输入YYYY-MM-DD格式）', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')


class StudentsListForm(FlaskForm):
    name = StringField('姓名（老师您测试的时候随便输入都可以）', validators=[DataRequired(), Length(1, 64)])
    number = StringField('学号（老师您测试的时候随便输入都可以）', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')
