from app.collection.form import UploadUserImage


import os
from typing import Union


from flask import render_template
from flask import Blueprint
from flask import current_app
from flask import flash
from flask import url_for
from flask import redirect
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename


collect = Blueprint('collection', __name__)


@collect.route('/upload', methods=['GET','POST'])
def upload():
	upload_form = UploadUserImage(meta={'csrf': False})
	if upload_form.validate_on_submit():
		image: Union[FileField, None] = upload_form.upload.data
		if image is None:
			flash('Image was not submitted!', 'error')
			current_app.logger.warning('Image was not submitted.')
			return redirect(url_for('collection.upload'))
		filename: str = secure_filename(image.filename)
		file_path: str = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
		image.save(file_path)
		current_app.logger.info('The image was saved successfully.')
		return redirect(url_for('collection.upload'))
	else:
		return render_template('index.html', upload_form=upload_form)
