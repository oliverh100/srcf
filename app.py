from flask import Flask, render_template
from forms import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', title='home')


@app.route('/test')
def test():
    pdf_form = PDFForm()
    return render_template('test.html', title='test', pdf_form=pdf_form)


if __name__ == "__main__":
    app.run()
