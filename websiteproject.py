from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/home/")
def home():
	return render_template("index.html")

@app.route("/AssignmentOne/")
def assignmentone():
	return render_template("assignmentone.html")
	

if __name__ == "__main__":
	app.run(debug = True)