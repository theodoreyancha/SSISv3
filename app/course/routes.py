from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')

course = Blueprint('course', __name__, url_prefix='/main_menu/course_table')

@course.route('/course_add', methods=['post','get'])
def index():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    mycursor.execute('SELECT `Name` FROM college')
    data = mycursor.fetchall()
    if request.method == 'POST' and 'course_code' in request.form:
        course_code = request.form['course_code']
        course = request.form['course']
        college = request.form['college']
        mycursor.execute("INSERT INTO `course` (`Code`, `Name`, `College`) "
                         "VALUES (%s,%s,%s)",
                         (course_code, course, college))
        db.commit()
        return redirect("/main_menu/course_table")
    else:
        pass
    return render_template('course_add.html', data=data)

@course.route('/course_edit', methods=['post','get'])
def course_edit():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == 'POST' and "code" in request.form:
        old_code = request.form['old_code']
        code = request.form['code']
        name = request.form['name']
        college = request.form['college']

        query2 = f"UPDATE `course` SET `Code` = '{code}', `Name` = '{name}', `College` = '{college}' WHERE `Code` = '{old_code}'"
        mycursor.execute(query2)
        db.commit()
        return redirect("/main_menu/course_table")
    return redirect("/main_menu/course_table")

@course.route('/course_delete', methods=['post','get'])
def course_delete():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        course_code = request.form['currentRow']
        f = f"DELETE FROM course WHERE `Code` = '{course_code}'"
        mycursor.execute(f)
        db.commit()
    return course_code