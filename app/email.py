from flask_mail import Message
from flask import render_template
import app
from app import mail


app.config['VICTORY_MAIL_SUBJECT_PREFIX'] = '[Victory] '
app.config['VICTORY_MAIL_SENDER'] = 'Victory Admin <jobrunner@victorynetworks.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['VICTORY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['VICTORY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
