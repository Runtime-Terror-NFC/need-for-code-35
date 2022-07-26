from flask import Flask,render_template
import sqlite3

app = Flask('__name__')

@app.route('/')
def main():
    return 'hello'

@app.route('/login')
def login():
    return 'login'

@app.route('/student')
def student_page():
    return 'student page'

@app.route('/teacher')
def teacher_page():
    return 'teacher page'

app.run()