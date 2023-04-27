from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired

class NewPropertyForm(FlaskForm):
    title = StringField('Title', validators=[])
    bedrooms = StringField('Number of Bedrooms', validators=[])
    bathrooms = StringField('Number of Bathrooms', validators=[])
    location = StringField('Location', validators=[])
    price = StringField('Price', validators=[])
    type = SelectField('Type', choices=[('House'), ('Apartment')])
    description = TextAreaField('Description', validators=[])
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    
    
    