from flask import Flask,render_template,request
import sqlite3

app = Flask('__name__')
app.config['SECRET_KEY'] = 'secretsecret'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        connection = sqlite3.connect('login.db')
        email = request.form.get('email')
        password = request.form.get('password')
        return email+" "+password
    return render_template('login.html')

@app.route('/student',methods=["POST","GET"])
def student_page():
    return 'student-page.html'

@app.route('/teacher')
def teacher_page():
    return render_template('teacher-page.html')

app.run()