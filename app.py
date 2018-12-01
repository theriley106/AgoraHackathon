from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session, send_file
import os
import random
import glob

app = Flask(__name__, static_url_path='/static')
CARDS = glob.glob("static/cards/*")
ACTIVE_CARDS = CARDS
DEALT_CARDS = []

@app.route('/', methods=['GET'])
def index():
	try:
		from keys import *
	except:
		AGORA_KEY = os.environ.get('API_KEY', None)
	return render_template("index.html", API_KEY=AGORA_KEY)

@app.route('/card', methods=["GET"])
def getCard():
	#print ACTIVE_CARDS
	a = random.choice(ACTIVE_CARDS)
	ACTIVE_CARDS.remove(a)
	filename = a
	return send_file(filename, mimetype='image/png')

@app.route('/reset', methods=["GET"])
def resetCards():
	while len(ACTIVE_CARDS) > 0:
		ACTIVE_CARDS.pop()
	while len(DEALT_CARDS) > 0:
		DEALT_CARDS.pop()
	for val in glob.glob("static/cards/*"):
		ACTIVE_CARDS.append(val)
	return jsonify({})

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
