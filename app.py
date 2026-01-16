from flask import Flask, render_template, abort, redirect, request, jsonify, url_for
from flask_cors import CORS
from datetime import datetime
import pytz
import uuid

app = Flask(__name__)
CORS(app)

# Store work orders in memory (or use a database)
work_orders = []

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

# ECE1181 Page
@app.route("/courses/ECE2170")
def ece2170():
    return render_template("courses/ECE2170/index.html", title_extention="ECE1181 - ")

# Lab0 Page
@app.route("/courses/ECE2170/revised-lab")
def ece2170labnew():
    return render_template("courses/ECE2170/LabNew.html", title_extention="Lab - ")



# Previous Labs
@app.route("/courses/ECE1181/previous-labs")
def ece1181previouslabs():
    return render_template("courses/ECE1181/previouslabs.html", title_extention="ECE1181 - ")

# Lab Guide Page
@app.route("/courses/ECE1181/lab-guide")
def ece1181labguide():
    return render_template("courses/ECE1181/labguide.html", title_extention="ECE1181 - ")

# Lab Guide Page
@app.route("/courses/ECE1181/cheat-sheet")
def ece1181lcheatsheet():
    return render_template("courses/ECE1181/cheatsheet.html", title_extention="ECE1181 - ")

# Lab0 Page
@app.route("/courses/ECE1181/lab-0")
def ece1181lab0():
    return render_template("courses/ECE1181/Lab0.html", title_extention="Lab 0 - ")

# Lab1 Page
@app.route("/courses/ECE1181/lab-1")
def ece1181lab1():
    return render_template("courses/ECE1181/Lab1.html", title_extention="Lab 1 - ")

# Lab2 Page
@app.route("/courses/ECE1181/lab-2")
def ece1181lab2():
    return render_template("courses/ECE1181/Lab2.html", title_extention="Lab 2 - ")

# Lab3 Page
@app.route("/courses/ECE1181/lab-3")
def ece1181lab3():
    return render_template("courses/ECE1181/Lab3.html", title_extention="Lab 3 - ")

# Lab4 Page
@app.route("/courses/ECE1181/lab-4")
def ece1181lab4():
    return render_template("courses/ECE1181/Lab4.html", title_extention="Lab 4 - ")

# Lab5 Page
@app.route("/courses/ECE1181/lab-5")
def ece1181lab5():
    return render_template("courses/ECE1181/Lab5.html", title_extention="Lab 5 - ")

# Lab6 Page
@app.route("/courses/ECE1181/lab-6")
def ece1181lab6():
    return render_template("courses/ECE1181/Lab6.html", title_extention="Lab 6 - ")

# Lab7 Page
@app.route("/courses/ECE1181/lab-7")
def ece1181lab7():
    return render_template("courses/ECE1181/Lab7.html", title_extention="Lab 7 - ")


# Lab8 Page
@app.route("/courses/ECE1181/lab-8")
def ece1181lab8():
    return render_template("courses/ECE1181/Lab8.html", title_extention="Lab 8 - ")

# Project Page
@app.route("/courses/ECE1181/final-project")
def ece1181project():
    return render_template("courses/ECE1181/FinalProject.html", title_extention="Project - ")



# Ethics Essay Page
@app.route("/projects/ethics-essay")
def ethics():
    return render_template("projects/ethics-essay.html", title_extention="Ethics Essay - ")

# Membrane Page
@app.route("/projects/membrane")
def membrane():
    return render_template("projects/membrane.html", title_extention="Membrane - ")

# Book Folding Page
@app.route("/projects/book-folding")
def bookfolding():
    return render_template("projects/book-folding.html", title_extention="Book Folding - ")

# Steno Recap Page
@app.route("/projects/one-year-steno")
def oys():
    return render_template("projects/one-year-steno.html", title_extention="Steno - ")

# Terminal Page
@app.route("/courses/conquering-the-terminal")
def ctt():
    return render_template("courses/ctt.html", title_extention="CtT - ")

# Devlog Page
@app.route("/projects/magnet-game/devlog-1")
def mgdl1():
    return render_template("projects/magnet-game/mg-devlog-1.html", title_extention="Magnet Game - ")

# Devlog Page
@app.route("/projects/magnet-game/devlog-2")
def mgdl2():
    return render_template("projects/magnet-game/mg-devlog-2.html", title_extention="Magnet Game - ")

# Devlog Page
@app.route("/projects/magnet-game/devlog-3")
def mgdl3():
    return render_template("projects/magnet-game/mg-devlog-3.html", title_extention="Magnet Game - ")

# Devlog Page
@app.route("/projects/magnet-game/devlog-4")
def mgdl4():
    return render_template("projects/magnet-game/mg-devlog-4.html", title_extention="Magnet Game - ")

# Feedback Box
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

# Workorder
@app.route('/submit_workorder', methods=['POST'])
def submit_workorder():
    issue = request.form.get('issue')
    if issue:
        work_orders.append({
            'id': str(uuid.uuid4()),
            'issue': issue,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify({'message': 'Request submitted successfully'})

@app.route('/ta-dashboard')
def dashboard():
    return render_template('courses/ECE1181/tadashboard.html', work_orders=work_orders)

@app.route('/resolve/<work_id>', methods=['POST'])
def resolve(work_id):
    global work_orders
    work_orders = [wo for wo in work_orders if wo['id'] != work_id]
    return jsonify({'status': 'success'})

# Terminal Page
@app.route("/projects/the-coopshap-story")
def coopshapstory():
    return render_template("projects/coopshap-story.html", title_extention="Story - ")


# Terminal Page
@app.route("/projects/magnet-game")
def maggame():
    return render_template("projects/magnet-game/index.html", title_extention="Magnet Game - ")








# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title_extention="404 - "), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


