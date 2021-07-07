from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from booktetium.factory import create_app

app = create_app()
app.config.from_object('booktetium.config')

db = SQLAlchemy(app)

@app.route('/', endpoint="index")
def main_page():
    return render_template("index.jinja2")


@app.route('/about')
def about():
    return render_template("about.jinja2")


@app.route('/contact')
def contact():
    return render_template("contact.jinja2")


@app.route('/courses')
def courses():
    return render_template("courses.jinja2")


@app.route('/events')
def events():
    return render_template("events.jinja2")


@app.route('/pricing')
def pricing():
    return render_template("pricing.jinja2")


@app.route('/trainers')
def trainers():
    return render_template("trainers.jinja2")


@app.route('/course-details', endpoint="course-details")
def course_details():
    return render_template("course-details.jinja2")


if __name__ == '__main__':
    app.run()
