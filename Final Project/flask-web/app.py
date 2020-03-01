#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2019/12/20
# @Author  : Liu Hanwen
# @File    : app.py

from __future__ import unicode_literals

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from Forms import EventListForm, StudentsListForm
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "hw"
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)


class Students(db.Model):
    __tablename__ = 'students'
    # primary_key 主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Date, default=datetime.date.today())

    def __init__(self, name, number):
        self.name = name
        self.number = number


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    # nullable 可空
    stu_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    event = db.Column(db.String(1024), nullable=False)
    value = db.Column(db.String(1024), nullable=False)
    event_time = db.Column(db.String(1024), nullable=False)
    create_time = db.Column(db.Date, default=datetime.date.today(), nullable=True)

    def __init__(self, stu_id, event, value, event_time):
        self.stu_id = stu_id
        self.event = event
        self.value = value
        self.event_time = event_time


@app.route('/', methods=['GET', 'POST'])
def show_students_list():
    form = StudentsListForm()
    db.create_all()
    if request.method == 'GET':
        # query.all()返回查询到的所有对象
        stulists = Students.query.all()
        return render_template('index.html', stulists=stulists, form=form)
    else:
        if form.validate_on_submit():
            entlist = Students(form.name.data, form.number.data)
            # add()插入数据
            db.session.add(entlist)
            # commit()提交事务
            db.session.commit()
            flash('你已经成功添加一个新的学生信息！')
        else:
            flash(form.errors)
        return redirect(url_for('show_students_list'))


@app.route('/delete/<int:id>')
def delete_student_list(id):
    # first_or_404() 返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应
    deleteStulist = Students.query.filter_by(id=id).first_or_404()
    # delete() 删除数据
    db.session.delete(deleteStulist)
    db.session.commit()
    flash('你成功删除一个学生的信息！')
    return redirect(url_for('show_students_list'))


@app.route('/view/<int:stu_id>', methods=['GET', 'POST'])
def show_event_list(stu_id):
    form = EventListForm()
    if request.method == 'GET':
        # filter_by() 过滤器
        Eventlists = Event.query.filter_by(stu_id=stu_id).join(Students, Event.stu_id == Students.id)
        return render_template('view.html', Eventlists=Eventlists, form=form)
    else:
        if form.validate_on_submit():
            Eventlist = Event(stu_id, form.event.data, form.value.data, form.event_time.data)
            # add()插入数据
            db.session.add(Eventlist)
            # commit()提交事务
            db.session.commit()
            flash('你已经成功添加一个新的活动')
        else:
            flash(form.errors)
        return redirect(url_for('show_event_list', _external=True, stu_id=stu_id))


@app.route('/change/<int:stu_id>/<int:id>', methods=['GET', 'POST'])
def change_event_list(stu_id, id):
    if request.method == 'GET':
        Eventlists = Event.query.filter_by(stu_id=stu_id, id=id).join(Students,
                                                                      Event.stu_id == Students.id).first_or_404()
        form = EventListForm()
        form.event.data = Eventlists.event
        form.value.data = Eventlists.value
        form.event_time.data = Eventlists.event_time
        return render_template('modify.html', form=form)
    else:
        form = EventListForm()
        if form.validate_on_submit():
            Eventlists = Event.query.filter_by(stu_id=stu_id, id=id).join(Students,
                                                                          Event.stu_id == Students.id).first_or_404()
            Eventlists.event = form.event.data
            Eventlists.value = form.value.data
            Eventlists.event_time = form.event_time.data
            db.session.add(Eventlists)
            db.session.commit()
            flash('你成功修改该学生活动情况！')
        else:
            flash(form.errors)
        return redirect(url_for('show_event_list', _external=True, stu_id=stu_id))


@app.route('/delete/<int:stu_id>/<int:id>')
def delete_event_list(stu_id, id):
    Eventlists = Event.query.filter_by(stu_id=stu_id, id=id).join(Students,
                                                                  Event.stu_id == Students.id).first_or_404()
    db.session.delete(Eventlists)
    db.session.commit()
    flash('你成功删去一个活动！')
    return redirect(url_for('show_event_list', _external=True, stu_id=stu_id))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
