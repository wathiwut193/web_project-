from flask import Flask
from flask_pymongo import PyMongo
from flask import Flask, render_template

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb+srv://wathiwut193:<Cc2191996>@cluster0-pjudc.mongodb.net/test?retryWrites=true'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/advanced_search')
def advanced_search():
    return render_template('advanced_search.html')


if __name__ == '__main__':
    app.run(debug=True)
