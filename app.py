from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photos')
def photos():
    print("Photos page accessed")
    return render_template('photos.html')


@app.route('/floral')
def floral():
    print("Florals page accessed")
    return render_template('floral.html')

@app.route('/writing')
def publications():
    print("Writing page accessed")
    return render_template('writing.html')

@app.route('/questions')
def questions():
    print("Questions page accessed")
    return render_template('questions.html')

@app.route('/lexicon')
def lexicon():
    print("Lexicon page accessed")
    return render_template('lexicon.html')

if __name__== '__main__':
    app.run(debug=True, host ='0.0.0.0', port = 9000)