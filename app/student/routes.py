from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')

student = Blueprint('student', __name__, url_prefix='/main_menu/student_table')

@student.route('/student_add', methods=['post','get'])
def index():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    mycursor.execute('SELECT `Course Name` FROM course')
    data = mycursor.fetchall()

    if request.method == 'POST' and 'student_id' in request.form:
        student_id = request.form['student_id']
        name = request.form['name']
        year_level = request.form['year_level']
        gender = request.form['gender']
        course = request.form['course']
        mycursor.execute("INSERT INTO `student` (`ID`, `Name`, `Year`, `Gender`, `Course`) "
                         "VALUES (%s,%s,%s,%s,%s)",
                         (student_id, name, year_level, gender, course))
        db.commit()
        return redirect("/main_menu/student_table")
    else:
        pass
    return render_template('student_add.html', data=data)


@student.route('/student_edit', methods=['post','get'])
def student_edit():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    if request.method == 'POST' and "student_id" in request.form:
        old_student_id = request.form['old_student_id']
        student_id = request.form['student_id']
        photo = request.files['photo']
        name = request.form['name']
        year_level = request.form['year_level']
        gender = request.form['gender']
        course = request.form['course']

        try:
            result = cloudinary.uploader.upload(photo)
            url = result.get('url')
            query2 = f"UPDATE `student` SET `ID` = '{student_id}', `Profile URL` = '{url}', `Name` = '{name}', `Year` = '{year_level}', `Gender` ='{gender}', `Course` = '{course}' WHERE `ID` = '{old_student_id}'"
            mycursor.execute(query2)
            db.commit()
            return redirect("/main_menu/student_table")
        except:
            query2 = f"UPDATE `student` SET `ID` = '{student_id}', `Profile URL` = '{url}', `Name` = '{name}', `Year` = '{year_level}', `Gender` ='{gender}', `Course` = '{course}' WHERE `ID` = '{old_student_id}'"
            mycursor.execute(query2)
            db.commit()
            return redirect("/main_menu/student_table")
    return redirect("/main_menu/student_table")

@student.route('/student_delete', methods=['post','get'])
def student_delete():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        student_id = request.form['currentRow']
        f = f"DELETE FROM student WHERE `ID` = '{student_id}'"
        mycursor.execute(f)
        db.commit()
    return student_id

@student.route('/student_image_clear', methods=['post','get'])
def student_image_clear():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        student_id = request.form['currentRow']
        f = f"UPDATE student SET `Profile URL` = NULL WHERE `ID` = '{student_id}'"
        mycursor.execute(f)
        db.commit()
    return student_id