from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')

college = Blueprint('college', __name__, url_prefix='/main_menu/college_table')

@college.route('/college_add', methods=['post','get'])
def index():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    if request.method == 'POST' and 'college_code' in request.form:
        college_code = request.form['college_code']
        college = request.form['college']
        mycursor.execute("INSERT INTO `college` (`Code`, `Name`) "
                         "VALUES (%s,%s)",
                         (college_code, college))
        db.commit()
        return redirect("/main_menu/college_table")
    else:
        pass
    return render_template('college_add.html')

@college.route('/college_edit', methods=['post','get'])
def college_edit():
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

        query2 = f"UPDATE `college` SET `Code` = '{code}', `Name` = '{name}' WHERE `Code` = '{old_code}'"
        mycursor.execute(query2)
        db.commit()
        return redirect("/main_menu/college_table")
    return redirect("/main_menu/college_table")

@college.route('/college_delete', methods=['post','get'])
def college_delete():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )

    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        college_code = request.form['currentRow']
        f = f"DELETE FROM college WHERE `Code` = '{college_code}'"
        mycursor.execute(f)
        db.commit()
    return college_code