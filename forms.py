from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class MenuForm(FlaskForm):
    test_page = SubmitField('Go to test page')


class PDFForm(FlaskForm):
    pdf = FileField(validators=[FileRequired()])
