from flask import Flask, request , make_response, redirect, render_template

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    information = ['php', 'python', 'Java']
    user_ip = request.cookies.get('user_ip')
    data = {
        'title': 'Index_Flask',
        'courses': information,
        'number_of_courses': len(information),
        'user_ip': user_ip
    }
    return render_template('base.html', data=data)


