import json, urllib, os, time
from flask import Flask, render_template, jsonify, request, redirect, url_for, send_file, g
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from app.models import Scouts
from app import app, celery, db
from app.calc import *
from app.scout import *


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def check_status(task):
	state = init_scout.AsyncResult(task).state
	return state

@celery.task
def init_scout(path, result_file, error_file):
	result = run_scout(path, result_file, error_file)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/search', methods=['GET'])
def search():
    return render_template("search.html")

@app.route('/search', methods=['POST'])
def search_post():
	try:
		asin = request.form['asin']
		if len(request.form['asin']) == 12:
			asin = upc_to_asin(request.form['asin'])[0]
		result = lookup_asin_data(asin)
		return render_template("lookup_results.html", data=result)
	except urllib.error.HTTPError:
		return render_template("search.html", error="http")
	except Exception as e:
		return render_template("search.html", error="fail", e=e)

@app.route('/upload', methods=["GET"])
def init():
    return render_template('upload.html')

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
	# Get the name of the uploaded file
	file = request.files['file']
	if file and allowed_file(file.filename):
		# Make the filename safe
		filename = secure_filename(file.filename)
		filename = os.path.splitext(filename)[0]
		# Get the date and time for filename ext
		now = time.strftime("%m%d%Y%H%M%S", time.localtime(time.time()))
		save_file = filename + '_' + now + '.csv'
		result_file = filename + '_results_' + now + '.csv'
		error_file = filename + '_errors_' + now + '.csv'
		# Move the file to the upload folder
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], save_file))
		task = init_scout.delay(os.path.join(app.config['UPLOAD_FOLDER'], save_file), result_file, error_file)
		status = init_scout.AsyncResult(task.id).state
		add_scout = Scouts(task.id, save_file, result_file, error_file, status)
		db.session.add(add_scout)
		db.session.commit()
		return redirect(url_for('scout_results'))
	else:
		return render_template("upload.html", error="fail")

@app.route('/results')
def scout_results():
	for scout in Scouts.query.order_by('-id').limit(10):
		if scout.status != 'SUCCESS':
			status = init_scout.AsyncResult(scout.task_id).state
			scout.status = status
			db.session.commit()
	return render_template("upload_results.html", Scouts=Scouts.query.order_by('-id').limit(10))

@app.route('/results/<result_file>')
def download_result_file(result_file):
    return send_file('files/results/' + result_file)

@app.route('/errors/<error_file>')
def download_error_file(error_file):
    return send_file('files/errors/' + error_file)

@app.route("/email")
def send_email():
	msg = Message('Hello', sender='you@dgoogle.com', recipients=['recipient@recipient_domain.com'])
	msg.body = "This is the email body"
	mail.send(msg)
	return "Sent"