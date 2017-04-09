from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Role class
class Events(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	campus = db.Column(db.String())
	location = db.Column(db.String())
	title = db.Column(db.String())
	date = db.Column(db.String())
	start = db.Column(db.String())
	end = db.Column(db.String())
	description = db.Column(db.String())
	tags = db.Column(db.String())
	
db.create_all()

@app.route('/api/visitors')
def thisstopsitfromcrashingforsomereason():
    content = request.json

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(host='localhost', port=port, debug=True)