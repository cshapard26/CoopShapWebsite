from flask import Flask, render_template, abort, redirect, request, jsonify
from flask_cors import CORS
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)

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

# Previous Labs
@app.route("/courses/ECE1181/previous-labs")
def ece1181previouslabs():
    return render_template("courses/ECE1181/previouslabs.html", title_extention="ECE1181 - ")

# Lab1 Page
@app.route("/courses/ECE1181/lab-1-getting-started")
def ece1181lab1():
    return render_template("courses/ECE1181/Lab1.html", title_extention="Lab 1 - ")

# Lab2 Page
@app.route("/courses/ECE1181/lab-2-tooling-up")
def ece1181lab2():
    return render_template("courses/ECE1181/Lab2.html", title_extention="Lab 2 - ")

# Terminal Page
@app.route("/courses/conquering-the-terminal")
def ctt():
    return render_template("courses/ctt.html", title_extention="CtT - ")


@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    try:
        # Retrieve the JSON data sent by the frontend
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing or invalid JSON data'}), 400

        feedback_content = data.get('feedback', '').strip()
        if not feedback_content:
            return jsonify({'error': 'No feedback provided'}), 400

        url = data.get('url', '')
        # Get the user's IP and current timestamp
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        timestamp = datetime.now(pytz.timezone('America/Chicago')).strftime('%Y-%m-%d %H:%M:%S')

        # Save feedback in a file
        with open('feedback.log', 'a') as file:
            file.write(f"{timestamp} | {user_ip} | {url} | {feedback_content}\n")

        return jsonify({'message': 'Feedback submitted successfully'})

    except Exception as error:
        return jsonify({'error': 'Something went wrong', 'details': str(error)}), 500


# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title_extention="404 - "), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


