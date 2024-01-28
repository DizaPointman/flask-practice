from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Schwanz Bandelin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Dickhead McDingDong'},
            'body': 'We need more porn on this site!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
