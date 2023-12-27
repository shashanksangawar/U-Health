# Importing Libraries
from flask import Flask, render_template, request
from flask_cors import CORS
import os, secrets
from supporting.heart import heart_prediction
# Configuration for Flask App
app = Flask(__name__)
CORS(app)
app._static_folder = "templates/static/"
app.secret_key = secrets.token_hex(16)

# Directory Path of current file 
source_path = os.path.dirname(__file__)
source_path = str(source_path)


# --------------------------------
# --------- Front-end ------------
# --------------------------------

# Index Page
@app.route('/')
def ui_main_page():
    return render_template('index.html')

# Heart Disease Prediction
@app.route('/heart_disease')
def ui_heart_disease():
    return render_template('heart.html')


# --------------------------------
# --------- Back-end ------------
# --------------------------------
@app.route('/api/heart_disease')
def api_heart_disease():
    return heart_prediction()


@app.route('/test')
def test():
    return "<h1> Test Approved from U-Health </h1>"


if __name__ == '__main__':
    app.run(debug=True)