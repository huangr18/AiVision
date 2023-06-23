from upload import app
from flask import render_template
from upload.models import User
from upload.models import UploadFileForm
from werkzeug.utils import secure_filename
import os

app.config['SECRET_KEY'] = 'abc123'
app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    users = User.query.all()
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data #grab file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  #save file
        return 'file has been uploaded'
    return render_template('upload.html', users=users, form=form)

