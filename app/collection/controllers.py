from app.collection.form import UploadUserImage


import os


from flask import Blueprint
from flask import current_app
from werkzeug.utils import secure_filename


collect = Blueprint('collection', __name__)


@collect.route('/upload', methods=['GET','POST'])
def upload():
	upload_form = UploadUserImage(meta={'csrf': False})
	if upload_form.validate_on_submite():
		filename: str = secure_filename(form.fileName.file.filename)
		file_path: str = os.path.join(current_app.config('UPLOAD_FOLDER'), filename)
		upload_form.fileName.file.save(file_path)
