from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session, send_file
import os
import random
import glob

app = Flask(__name__, static_url_path='/static')
CARDS = glob.glob("static/cards/*")
ACTIVE_CARDS = CARDS
DEALT_CARDS = []
MOST_RECENT = []
LAST_SENT = []

@app.route('/', methods=['GET'])
def index():
	try:
		from keys import *
	except:
		AGORA_KEY = os.environ.get('API_KEY', None)
	return render_template("index.html", API_KEY=AGORA_KEY)

@app.route('/recent', methods=["GET"])
def getMostRecent():
	while len(LAST_SENT) > 0:
		LAST_SENT.pop()
	file = MOST_RECENT[-1]
	LAST_SENT.append(file)
	return send_file(file, mimetype='image/png')

@app.route('/card', methods=["GET"])
def getCard():
	#print ACTIVE_CARDS
	a = random.choice(ACTIVE_CARDS)
	ACTIVE_CARDS.remove(a)
	filename = a
	MOST_RECENT.append(filename)
	#LAST_SENT.append(filename)
	return send_file(filename, mimetype='image/png')

@app.route('/reset', methods=["GET"])
def resetCards():
	print("CARDS HAVE BEEN RESET")
	while len(ACTIVE_CARDS) > 0:
		ACTIVE_CARDS.pop()
	while len(DEALT_CARDS) > 0:
		DEALT_CARDS.pop()
	for val in glob.glob("static/cards/*"):
		ACTIVE_CARDS.append(val)
	return jsonify({})

@app.route('/isNew', methods=["GET"])
def checkNew():
	try:
		return str(LAST_SENT[-1] != MOST_RECENT[-1]).lower()
	except Exception as exp:
		print exp
		return exp

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
