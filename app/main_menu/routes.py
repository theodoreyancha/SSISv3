from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')

main_menu = Blueprint('main_menu', __name__, url_prefix='/main_menu')

@main_menu.route('/')
def index():
    return render_template('ssis_main.html')

@main_menu.route('/student_table', methods=['post','get'])
def students():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM student')
    data = mycursor.fetchall()
    return render_template('student_table.html', data=data)

@main_menu.route('/course_table', methods=['post','get'])
def course():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM course')
    data = mycursor.fetchall()
    return render_template('course_table.html', data=data)

@main_menu.route('/college_table', methods=['post','get'])
def college():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM college')
    data = mycursor.fetchall()
    return render_template('college_table.html', data=data)