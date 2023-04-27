from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TranslateForm(FlaskForm):
    target_lang = SelectField('Select target language', choices=[("", ""), ("DE", "German"), ("EN-GB", "English (British)"), ("ES", "Spanish"), ("FI", "Finnish"), 
                                                          ("IT", "Italian"), ("JA", "Japanese"), ("NB", "Norwegian Bokmal"), ("PL", "Polish"), ("RU", "Russian"), ("ZH", "Chinese")])
    userInput = StringField('Username', validators=[DataRequired()])
    output = StringField('Output')
    submit = SubmitField('Translate')