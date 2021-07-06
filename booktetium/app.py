from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', endpoint="index")
def main_page():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")

@app.route('/trainers')
def trainers():
    return render_template("trainers.html")

@app.route('/course-details', endpoint="course-details")
def course_details():
    return render_template("course-details.html")

if __name__ == '__main__':
    app.run()
