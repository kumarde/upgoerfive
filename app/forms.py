from flask.ext.wtf import Form
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required

class QueryForm(Form):
  sentence = TextAreaField('Sentence', validators=[Required()],
              default='He yearned to engage in difficult labor')

