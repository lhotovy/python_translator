from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TranslateForm(FlaskForm):
    userInput = StringField('Username', validators=[DataRequired()])
    output = StringField('Output')
    submit = SubmitField('Translate')