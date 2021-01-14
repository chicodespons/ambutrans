import datetime

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/2")
def index2():
	headline = "Hello, world"
	return render_template("index.html", headline=headline)

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()

@app.route("/bye")
def bye():
	headline = "Goodbye!"
	return render_template("index.html", headline=headline)


@app.route("/newyear")
def newyear():
	now = datetime.datetime.now()
	#boelean 
	new_year = now.month == 1 and now.day == 1
	return render_template("newyear.html", new_year=new_year)

@app.route("/loops")
def loops():
	names = ["Alice", "Bob", "Charlie"]
	return render_template("loops.html", names= names)

#linking pages + inheritence templates met layout.html

@app.route("/page1")
def page1():
	return render_template("page1.html")

@app.route("/page2")
def page2():
	return render_template("page2.html")


# forms (import request vanboven file)

@app.route("/input")
def input():
	return render_template("input.html")

@app.route("/form", methods=["POST"])
def form():
	name = request.form.get("name")
	return render_template("form.html", name=name)

#idien je form direct wil opvragen(is dus een get method)
#@app.route("/form", methods=["GET", "POST"])
#def form():
#    if request.method == "GET":
#       return "Please submit the form insted"
#    else:
#         name = request.form.get("name")
#         return render_template("form.html", name=name)


# sessions( data specifiek to your account)
#vanboven import session
# maar ook from flask_session import Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/session1", methods=["GET", "POST"])
def session1():
	session["notes"] = []
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("session1.html", notes=session["notes"])
