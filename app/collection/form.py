from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class UploadUserImage(FlaskForm):
	upload = FileField('image', validators=[
		FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
