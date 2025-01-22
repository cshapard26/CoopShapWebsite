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

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html", title_extention="Contact - ")

# Labs Page
@app.route("/labs")
def labs():
    return render_template("labs/index.html", title_extention="Labs - ")

# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title_extention="404 - "), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


