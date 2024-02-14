from palettemaker import PaletteMaker
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, BooleanField
from werkzeug.utils import secure_filename
from PIL import UnidentifiedImageError
import os

# Init Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_KEY']


palette = PaletteMaker()

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder


class ImageForm(FlaskForm):
    image = FileField('Choose Image', validators=[FileAllowed(['jpg']), FileRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=["GET", "POST"])
def home():
    form = ImageForm()
    if form.is_submitted():
        try:
            file = form.image.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
            image = os.path.join(app.config['UPLOAD'], filename)
            hex_codes = palette.analyze_image(image)
            return render_template("index.html", image=image, hex_codes=hex_codes, form=form)
        except UnidentifiedImageError:
            image = ""
            hex_codes = []
            return render_template("index.html", image=image, hex_codes=hex_codes, form=form)
    else:
        image = ""
        hex_codes = []
        return render_template("index.html", image=image, hex_codes=hex_codes, form=form)


if __name__ == "__main__":
    app.run(debug=True)