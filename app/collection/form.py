from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_upload import UploadSet, IMAGES

images = UploadSet('images', IMAGES)

class UploadUserImage(FlaskForm):
	upload = FileField('image', validators=[
		FileAllowed(images, 'Images only!')])
	