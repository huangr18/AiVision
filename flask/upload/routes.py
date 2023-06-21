from upload import app
from flask import render_template
from upload.models import User

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    users = User.query.all()
    return render_template('upload.html', users=users)

