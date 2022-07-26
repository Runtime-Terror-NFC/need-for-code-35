from flask import Flask,render_template,request,redirect,session
import sqlite3
import marks
app = Flask('__name__')
app.secret_key = 'secretsecret'
temp = 0

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        connection = sqlite3.Connection('login.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM login")
        result = cursor.fetchall()
        for i in range(len(result)):
            db_email = result[i][0]
            db_password = result[i][2]
            user_type = result[i][3]
            # print(db_email,db_password)
            if email == db_email and password == db_password:
                if user_type == 'student':
                    return redirect('/student')
                elif user_type == 'teacher':
                    return redirect('/teacher')
            else:
                render_template('login.html',flag="Invalid Credentials")

    return render_template('login.html')

@app.route('/student',methods=["POST","GET"])
def student_page():
    return render_template('student-page.html')

@app.route('/teacher',methods=["GET","POST"])
def teacher_page():
    if request.form.get=='POST':
        return "teacher"
    return render_template('teacher-page.html')

@app.route('/admin')
def admin():
    return render_template('admin-page.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
    
@app.route('/contact',methods=["GET","POST"])
def contact():
    return render_template('contact.html')

app.run()