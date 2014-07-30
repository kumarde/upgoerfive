from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, BooleanField
from wtforms.validators import Required

class QueryForm(Form):
  sentence = TextAreaField('Sentence', validators=[Required()],
              default='He yearned to engage in difficult labor')

class InputForm(Form):
  input = TextField('Sentence', validators=[Required()])
