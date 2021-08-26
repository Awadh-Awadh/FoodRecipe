from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IngredientsForm(FlaskForm):
    ingredient1=StringField('First ingredient', validators=[DataRequired()])
    ingredient2 = StringField('Second ingredient', validators=[DataRequired()] )
    ingredient3=StringField('Third ingredient')
    submit = SubmitField('Search')