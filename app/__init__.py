from flask import Flask, redirect

import cloudinary
from os import getenv

from .main_menu.routes import main_menu
from .student.routes import student
from .course.routes import course
from .college.routes import college



app = Flask(__name__)

app.register_blueprint(main_menu)
app.register_blueprint(student)
app.register_blueprint(course)
app.register_blueprint(college)

def create_app():
    app = Flask(__name__)

    return app

cloudinary.config(
    cloud_name = getenv('CLOUD_NAME'),
    api_key = getenv('API_KEY'),
    api_secret = getenv('API_SECRET')
)