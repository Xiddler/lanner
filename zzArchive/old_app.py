#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	# INSERT new snippet
	data = request.form
	snippet = data.get('snippet', 'no message')
	conn = sqlite3.connect('snippets.db')
	# print("Database opened successfully")
	cur = conn.cursor()
	cur.execute("INSERT INTO snippets(snippet) values (?)", (snippet, ))
	# opt = cur.fetchall()
	# opt = cur.fetchone()
	conn.commit() 
	conn.close() 
	#	
	# OUTPUT new snippet
	conn = sqlite3.connect('snippets.db')
	# print("Opened database successfully")
	cur = conn.cursor()
	cur.execute("SELECT snippet FROM snippets ORDER BY id DESC; ")
	all_snippets = cur.fetchall()
	# fetchall() returns a row list
	# test = cur.fetchone()
	# most_recent = [item[0] for item in all_snippets[0:2]]
	most_recent1 = all_snippets[0:1][0][0]
	most_recent2 = all_snippets[1:2][0][0]
	conn.close()	
	# most_recent1 = snippet
	# most_recent2 = "this2"
	return render_template('index.html', most_recent1=most_recent1, most_recent2=most_recent2)

if __name__ == '__main__':
	app.run(host ='0.0.0.0', port=9000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.

