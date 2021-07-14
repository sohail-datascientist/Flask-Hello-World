from flask import Flask
app=Flask(__name__)

@app.route("/")

def Task_01():
	return "Hello World of Programmers"