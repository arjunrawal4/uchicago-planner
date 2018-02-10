from app import app, db
import logging
from flask import Flask, render_template, request
from app.models import User
from sqlalchemy import Table, Column, MetaData, DateTime
from sqlalchemy.orm import joinedload
log = logging.getLogger("webapp")

@app.route('/')
@app.route('/templates/index')
def index():
    users = db.session.query(User)
    log.info(users)
    return render_template('index.html', users=users)
