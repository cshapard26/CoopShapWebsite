from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html", title_extention="")

# About Page
@app.route("/about")
def about():
    return render_template("about.html", title_extention="About - ")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html", title_extention="Projects - ")

# Labs Page
@app.route("/courses")
def courses():
    return render_template("courses/index.html", title_extention="Labs - ")

# ECE1181 Page
@app.route("/courses/ECE1181")
def ece1181():
    return render_template("courses/ECE1181/index.html", title_extention="ECE1181 - ")

# Lab1 Page
@app.route("/courses/ECE1181/lab-1-getting-started")
def ece1181lab1():
    return render_template("courses/ECE1181/Lab1.html", title_extention="ECE1181 - ")

# Terminal Page
@app.route("/courses/conquering-the-terminal")
def ctt():
    return render_template("courses/ctt.html", title_extention="CtT - ")

# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title_extention="404 - "), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


