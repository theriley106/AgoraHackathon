from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import os

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	AGORA_KEY = os.environ.get('API_KEY', None)
	return render_template("index.html", API_KEY=AGORA_KEY)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
