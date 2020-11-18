from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField, BooleanField, TextAreaField, validators, Form, FloatField

class AddSkin(Form):
    name = StringField('Nombre Skin', [validators.DataRequired()])
    price = FloatField('Precio', [validators.DataRequired()])
    float = FloatField('Desgaste', [validators.DataRequired()])
    stock = IntegerField('Stock', [validators.DataRequired()])
    image = FileField('Imagen skin', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])