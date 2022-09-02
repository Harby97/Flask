from flask import Flask, request , make_response, redirect, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'CLAVE SECRETA'

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    # response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello', methods=['GET','POST'])
def hello():
    information = ['php', 'python', 'Java']
    user_ip = session.get('user_ip')
    # user_ip = request.cookies.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    data = {                #contexto
        'title': 'Index_Flask',
        'courses': information,
        'number_of_courses': len(information),
        'user_ip': user_ip,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        return redirect(url_for('index'))

    return render_template('base.html', data=data)


