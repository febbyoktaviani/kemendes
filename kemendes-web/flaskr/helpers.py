import datetime
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import current_app as app
from werkzeug.utils import secure_filename

def generate_password(app, password):
    bcrypt = Bcrypt(app)
    password_hash = bcrypt.generate_password_hash(password)
    return password_hash

def check_password(app, db_password, password):
    bcrypt = Bcrypt(app)
    is_match = bcrypt.check_password_hash(db_password, password)
    return is_match

def create_token(username):
    expires = datetime.timedelta(days=365)
    return create_access_token(identity=username, expires_delta=expires)

def authenticate_user():
    return get_jwt_identity()

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    filename = secure_filename(file.filename)
    file_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    served_url = os.path.join(app.config['STATIC_FOLDER'], filename)
    file.save(file_url)
    return served_url

    