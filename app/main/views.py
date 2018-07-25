from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import login_required
from .import main
#from .forms import NameForm
from .models.user import User


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

