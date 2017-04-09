from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Role class
class Events(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	campus = db.Column(db.String())
	location = db.Column(db.String())
	title = db.Column(db.String())
	date = db.Column(db.String())
	start = db.Column(db.String())
	end = db.Column(db.String())
	description = db.Column(db.String())
	tags = db.relationship("Tags", cascade="all, delete, delete-orphan")
	
class Tags(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	resultid = db.Column(db.Integer, db.ForeignKey('Events.id'))
	tag = db.Column(db.String(255))
db.create_all()
@app.route('/post', methods=['POST'])
def post():
	campus=request.form['dropdown']
	location=request.form['location']
	title = request.form['title']
	start=request.form['start']
	end=request.form['end']
	description=request.form['description']
	tags = request.form.getlist('tags')
	event = Events (campus = campus, location = location, title = title, start = start, end = end, description = description)
	for tag in tags:
		event.tags.append(Tags(tag = tag))
	if len(tags) == 0:
		event.tags.append(Tags(tag == "Other"))
	db.session.add(event)
	db.session.commit()
	
@app.route('/api/visitors')
def thisstopsitfromcrashingforsomereason():
    content = request.json

@app.route('/addForm')
def addForm():
	return render_template('addForm.html')
	
@app.route('/category')
def category():
	return render_template('category.html')
	
@app.route('/cal')
def cal():
	return render_template('cal.html')

@app.route('/home')
def home():
    return render_template('index.html')
	
@app.route('/')
def index():
    return render_template('index.html')
	
port = int(os.getenv('PORT', 8080))
if __name__ == '__main__':
	app.run(host='localhost', port=port, debug=True)